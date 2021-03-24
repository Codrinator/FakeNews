import preprocessing
import testing
import corpus
import classifiers_ioana as c_i
import data_models

if __name__ == "__main__":
    # Gather news from websites and separate in json files
    # scraper.scrape_data()

    # Get fake news and data news corpus
    true_news_corpus, fake_news_corpus = corpus.get_corpus()
    testing.get_corpus_word_count(true_news_corpus, fake_news_corpus)

    # Preprocess data and add to json files
    # preprocessing.preprocess_data(true_news_corpus, fake_news_corpus)

    # Get preprocessed data
    true_pre_data, fake_pre_data = preprocessing.get_preprocessed_data()
    testing.get_processed_data_word_count(true_pre_data, fake_pre_data)

    # Merge labeled data
    merged_labeled_data = preprocessing.merge_news(true_pre_data, fake_pre_data)

    # Get word_frequency
    word_frequency = preprocessing.get_word_frequency(merged_labeled_data)

    # Get vocabulary
    vocabulary = preprocessing.get_vocabulary(merged_labeled_data, word_frequency)

    # Try reducing data to specified number of articles
    new_merged_labeled_data, new_vocabulary, new_word_frequency = data_models.split_data_by_articles(vocabulary, word_frequency, merged_labeled_data, 500)
    #print(len(new_merged_labeled_data), len(new_vocabulary), len(new_word_frequency))

    # Try reducing data to specified number of articles
    new2_merged_labeled_data, new2_vocabulary, new2_word_frequency = data_models.split_data_by_percentage(vocabulary, word_frequency, merged_labeled_data, 50)
    #print(len(new2_merged_labeled_data), len(new2_vocabulary), len(new2_word_frequency))

    # Test NaiveBayes
    c_i.naive_bayes(vocabulary, word_frequency, merged_labeled_data)

