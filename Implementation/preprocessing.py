from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import numpy as np
import random
import math

# Romanian stemmer
RS = SnowballStemmer('romanian', ignore_stopwords=True)


def get_stopwords():
    """ Read stop words from .txt file """
    with open("DataFiles/stopwords.txt", encoding="utf-8") as f:
        stopwords = f.read().split()
    return stopwords


def tokenize_data(news_data, stop_words):
    """ Merge title and content, lower strings, tokenize, remove non-alpha characters, remove stop-words """
    tokenized_data = []
    for item in news_data.values():
        tokenized_data.append(item[0] + item[1])
    # Tokenize, remove stop-words
    for i in range(0,len(tokenized_data)):
        tokenized_data[i] = [index.lower() for index in word_tokenize(tokenized_data[i]) if index.isalpha()]
        tokenized_data[i] = [index for index in tokenized_data[i] if index not in stop_words]
    return tokenized_data


def stem_data(text):
    """ Apply NLTK Romanian stemmer on tokenized data """
    stemmed_data = []
    for item in text:
        stemmed_data.append([RS.stem(i) for i in item])
    for i in range(0,len(stemmed_data)):
        stemmed_data[i] = [index for index in stemmed_data[i] if len(index) < 18]
        stemmed_data[i] = [index for index in stemmed_data[i] if "ascultare" not in index]
        stemmed_data[i] = [index for index in stemmed_data[i] if "aplicații" not in index]
    return stemmed_data


def preprocess_category(news_data):
    """ Preprocess wither fake or true news data """
    stop_words = get_stopwords()
    tokenized_data = tokenize_data(news_data, stop_words)
    stemmed_data = stem_data(tokenized_data)
    return stemmed_data


def add_to_txt(text, file):
    """ Add list to .txt file as a string """
    with open(file, "w", encoding="utf-8") as f:
        f.write(str(text))


def preprocess_data(true, fake):
    """ """
    true_pre_category = preprocess_category(true)
    fake_pre_category = preprocess_category(fake)
    add_to_txt(true_pre_category, "DataFiles/truePreprocessedData.txt")
    add_to_txt(fake_pre_category, "DataFiles/fakePreprocessedData.txt")


def get_from_txt(file):
    """ Get list from a .txt file """
    with open(file, "r", encoding="utf-8") as f:
        text = eval(f.read())
    return text


def get_preprocessed_data():
    """ Return both categories of preprocessed data """
    true_pre_data = get_from_txt("DataFiles/truePreprocessedData.txt")
    fake_pre_data = get_from_txt("DataFiles/fakePreprocessedData.txt")
    return true_pre_data, fake_pre_data


def merge_news(true, fake):
    """ Merge true and fake news """
    merged_data = []
    for item in true:
        merged_data.append((1, item))
    for item in fake:
        merged_data.append((0, item))

    random.shuffle(merged_data)

    for item in range(0, len(merged_data)):
        merged_data[item] = [merged_data[item][0], merged_data[item][1]]

    return merged_data


def get_word_frequency(news_data):
    """ Count the apparitions of the vocabulary words """
    word_frequency = dict()
    for item in news_data:
        for word in item[1]:
            if word in word_frequency.keys():
                word_frequency[word] +=1
            else:
                word_frequency[word] = 1
    word_frequency = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}
    return word_frequency


def get_vocabulary(news_data, word_frequency):
    """ Make the vocabulary of a data category """
    vocabulary = dict()
    counter = 0
    for key in word_frequency.keys():
        vocabulary[key] = counter
        counter += 1
    return vocabulary


def one_hot(text, vocabulary):
    hot_vector = [0]*len(vocabulary)
    for word in text:
        if word in vocabulary.keys():
            hot_vector[vocabulary[word]] += 1
    return hot_vector


def bag_of_words(news_data, vocabulary):
    """ Count the apparitions of the vocabulary words """
    count_vectorizer = []
    for item in news_data:
        count_vectorizer.append([item[0], one_hot(item[1], vocabulary)])
    return count_vectorizer


def count_vectorizer_word_amount(news_data, vocabulary, number_of_words):
    """ Get BoW for a chosen number of words """
    new_vocabulary = dict()
    for key, value in vocabulary.items():
        if value < number_of_words:
            new_vocabulary[key] = value
    count_vectorizer = bag_of_words(news_data, new_vocabulary)
    return count_vectorizer


def count_vectorizer_word_count(news_data, word_frequency, vocabulary, minimum):
    """ Get BoW for words that appear at least a chosen number of times """
    new_vocabulary = dict()
    for key, value in word_frequency.items():
        if value >= minimum:
            new_vocabulary[key] = vocabulary[key]
    count_vectorizer = bag_of_words(news_data, new_vocabulary)
    return count_vectorizer


def get_vocabulary_word_count(true, fake):
    """ Pretty print the vocabulary sizes for each news category """
    print("\n   Vocabulary Word Counts")
    print("True news:", len(true))
    print("Fake news:", len(fake))


def tf_idf(count_vectorizer):
    """ TF-IDF implementation """
    total_words = len(count_vectorizer[0][1])

    # tf
    tf = []
    for index in range(len(count_vectorizer)):
        #article_words = len(merged_labeled_data[index][1])
        article_words = 0
        for word in count_vectorizer[index][1]:
            article_words += word
        article_tf = [count_vectorizer[index][0],[]]
        for word in count_vectorizer[index][1]:
            article_tf[1].append(word/(article_words+1))
        tf.append(article_tf)

    # df
    df = [0]*total_words
    for article in count_vectorizer:
        counter = 0
        for word in article[1]:
            if word > 0:
                df[counter] += 1
            counter += 1

    # idf
    idf = [math.log(len(count_vectorizer)/(i+1)) for i in df]

    # tf-idf
    tf_idf = []
    for article in tf:
        article_tf_idf = [article[0], []]
        counter = 0
        for word in article[1]:
            article_tf_idf[1].append(word * idf[counter])
            counter += 1
        tf_idf.append(article_tf_idf)

    return tf_idf