from sklearn.model_selection import train_test_split


def split_data_by_articles(vocabulary, word_frequency, merged_labeled_data, articles):
    """ Reduce data to specified number of articles"""
    counter = 0
    new_merged_labeled_data, new_vocabulary, new_word_frequency = [], dict(), dict()
    for key in vocabulary.keys():
        if counter < articles:
            new_merged_labeled_data.append(merged_labeled_data[counter])
            new_vocabulary[key] = vocabulary[key]
            new_word_frequency[key] = word_frequency[key]
            counter += 1
        else:
            break
    return new_merged_labeled_data, new_vocabulary, new_word_frequency


def split_data_by_percentage(vocabulary, word_frequency, merged_labeled_data, percentage):
    """ Reduce data to specified number of articles"""
    counter = 0
    max_counter = int(len(merged_labeled_data)/100*percentage)
    new_merged_labeled_data, new_vocabulary, new_word_frequency = [], dict(), dict()
    for key in vocabulary.keys():
        if counter < max_counter:
            new_merged_labeled_data.append(merged_labeled_data[counter])
            new_vocabulary[key] = vocabulary[key]
            new_word_frequency[key] = word_frequency[key]
            counter += 1
        else:
            break
    return new_merged_labeled_data, new_vocabulary, new_word_frequency


def split_test_train_data(data, percentage):
    """ Split data into testing and training based on chosen percentage """
    y = [item[0] for item in data]
    X = [item[1] for item in data]
    # Get training and testing vectors in X, labels in y
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=percentage)
    return X_train, X_test, y_train, y_test

def get_corpus_spaces(text):
    """ Roughly get initial number of words by counting spaces """
    space_count = 0
    for key, value in text.items():
        space_count += (value[0] + value[1]).count(" ")
    return space_count


def get_corpus_word_count(true, fake):
    """ Pretty print number of words for each initial news corpus """
    print("\n   True News\nNumber of articles:", len(true), "\nNumber of words:", get_corpus_spaces(true))
    print("\n   Fake News\nNumber of articles:", len(fake), "\nNumber of words:", get_corpus_spaces(fake))


def get_pre_word_count(news_data):
    """ Get number of words in the preprocessed data """
    word_count = 0
    for word in news_data:
        word_count += len(word)
    return word_count


def get_processed_data_word_count(true, fake):
    """ Pretty print numnber of words for the preprocessed data """
    print("\n   Preprocessed Word Counts")
    print("True news:", get_pre_word_count(true))
    print("Fake news:", get_pre_word_count(fake))


def get_vocabulary_size(text):
    """ Get the number of words in a vocabulary """
    words = 0
    for key, value in text.items():
        words += value
    return words


def get_vocabulary_word_count(true, fake):
    """ Pretty print the vocabulary sizes for each news category """
    print("\n   Vocabulary Word Counts")
    print("True news:", len(true))
    print("Fake news:", len(fake))