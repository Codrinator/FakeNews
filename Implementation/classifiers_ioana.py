from sklearn.naive_bayes import MultinomialNB
import preprocessing
import data_models


def naive_bayes(vocabulary, word_frequency, merged_labeled_data):
    """ Implement Naive Bayes and perform accuracy_tests """
    # Bag of words for first x words
    count_vectorizer_2000 = preprocessing.count_vectorizer_word_amount(merged_labeled_data, vocabulary, 2000)
    X_train, X_test, y_train, y_test = data_models.split_test_train_data(count_vectorizer_2000, 0.2)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print("\nNaive Bayes:", (y_test == pred).sum() * 100 / len(y_test),"% accuracy")