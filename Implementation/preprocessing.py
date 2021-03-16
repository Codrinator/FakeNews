from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize

# Romanian stemmer
RS = SnowballStemmer('romanian', ignore_stopwords=True)


def get_stopwords():
    """ Read stop words from .txt file """
    with open("DataFiles/stopwords.txt", encoding="utf-8") as f:
        stopwords = f.read().split()
    return stopwords


def tokenize_data(news_data, stop_words):
    """ Merge title and content, lower strings, tokenize, remove non-alpha characters, remove stop-words """
    tokenized_data = news_data
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


def get_vocabulary(news_data):
    """ Make the vocabulary of a data category """
    vocabulary = dict()
    for item in news_data:
        for word in item:
            if word not in vocabulary.keys():
                vocabulary[word] = 1
            else:
                vocabulary[word] += 1

    all_words = []
    for key in vocabulary.keys():
        all_words.append(key)
    return all_words

def preprocess_cv(news_data):
    """ Preprocess wither fake or true news data """
    stop_words = get_stopwords()
    tokenized_data = tokenize_data(news_data, stop_words)
    stemmed_data = stem_data(tokenized_data)
    return stemmed_data