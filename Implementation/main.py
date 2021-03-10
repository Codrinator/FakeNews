import preprocessing
import scraper
import testing
import corpus


if __name__ == "__main__":
    # Gather news from websites and separate in json files
    #scraper.scrape_data()

    # Get fake news and data news corpus
    true_news_corpus, fake_news_corpus = corpus.get_corpus()
    testing.get_corpus_word_count(true_news_corpus, fake_news_corpus)

    # Preprocess data and add to json files
    #preprocessing.preprocess_data(true_news_corpus, fake_news_corpus)

    # Get preprocessed data
    true_pre_data, fake_pre_data = preprocessing.get_preprocessed_data()
    testing.get_processed_data_word_count(true_pre_data, fake_pre_data)

    # Get news category vocabularies
    true_vocabulary = preprocessing.get_vocabulary(true_pre_data)
    fake_vocabulary = preprocessing.get_vocabulary(fake_pre_data)
    testing.get_vocabulary_word_count(true_vocabulary, fake_vocabulary)
