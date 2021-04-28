from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.mixture import GaussianMixture
from sklearn import svm
import preprocessing
import data_models


def classification(sample_data, test_percentage, classificator):
    """ Implement Logistic Regression and perform accuracy_tests """
    # Bag of words for first x words
    X_train, X_test, y_train, y_test = data_models.split_test_train_data(sample_data, test_percentage)
    logistic_clf = eval(classificator)
    logistic_clf.fit(X_train, y_train)
    pred = logistic_clf.predict(X_test)
    return (y_test == pred).sum() * 100 / len(y_test)


def voting_classifier(sample_data, test_percentage, classifiers):
    """ Use multiple classifiers """
    classifier_list = classifiers.split(",")
    classifier_list = [(i.split("(",1)[0],eval(i)) for i in classifier_list]
    voting_clf = VotingClassifier(estimators=classifier_list, voting='hard')
    X_train, X_test, y_train, y_test = data_models.split_test_train_data(sample_data, test_percentage)
    voting_clf.fit(X_train, y_train)
    pred = voting_clf.predict(X_test)
    return (y_test == pred).sum() * 100 / len(y_test)

