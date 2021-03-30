from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import PassiveAggressiveClassifier
import preprocessing
import data_models


def naive_bayes(sample_data, test_percentage):
    """ Implement Naive Bayes and perform accuracy_tests """
    # Bag of words for first x words
    X_train, X_test, y_train, y_test = data_models.split_test_train_data(sample_data, test_percentage)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    return(y_test == pred).sum() * 100 / len(y_test)


def passive_aggressive(sample_data, test_percentage):
    """ Implement Naive Bayes and perform accuracy_tests """
    # Bag of words for first x words
    X_train, X_test, y_train, y_test = data_models.split_test_train_data(sample_data, test_percentage)
    linear_clf = PassiveAggressiveClassifier()
    linear_clf.fit(X_train, y_train)
    pred = linear_clf.predict(X_test)
    return (y_test == pred).sum() * 100 / len(y_test)