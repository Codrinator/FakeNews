

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
