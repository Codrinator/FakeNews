import classifiers_ioana as c_i
import preprocessing


def average_classifier(function, test_data):
    """ Get the average accuracy and running time for a specific classifier, data and testing size """
    import time
    accuracy_sum = 0
    start_time = time.time()
    for i in range(100):
        result = eval(function)
        accuracy_sum += result
    accuracy_average = accuracy_sum/100
    return str(accuracy_average) + "%, " + str((time.time()-start_time)/100) + " seconds"


def test_classifier(classifier, classifier_function_name, vocabulary, merged_labeled_data):
    """ A model for testing all classifiers """
    print("\n   ***", classifier, "***")

    # Original data testing
    print("\nORIGINAL DATA",)
    print("  Number of articles:", len(merged_labeled_data))
    print("  Number of total words:", sum([len(item[1]) for item in merged_labeled_data]))
    print("  Number of distinct words:", len(vocabulary))
    # All words
    print("   ^ALL WORDS^")
    count_vectorizer_all = preprocessing.count_vectorizer_word_amount(merged_labeled_data, vocabulary, sum([1 for i in vocabulary.items()]))
    print("    Count vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", count_vectorizer_all))
    print("    Count vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", count_vectorizer_all))
    tf_idf_all = preprocessing.tf_idf(count_vectorizer_all)
    print("    TF-IDF vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", tf_idf_all))
    print("    TF-IDF vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", tf_idf_all))
    # Most popular 1000 words
    print("   ^FIRST 1000 WORDS^")
    count_vectorizer_1000 = preprocessing.count_vectorizer_word_amount(merged_labeled_data, vocabulary, 1000)
    print("    Count vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", count_vectorizer_1000))
    print("    Count vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", count_vectorizer_1000))
    tf_idf_1000 = preprocessing.tf_idf(count_vectorizer_1000)
    print("    TF-IDF vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", tf_idf_1000))
    print("    TF-IDF vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", tf_idf_1000))
    # Most popular 200 words
    print("   ^FIRST 200 WORDS^")
    count_vectorizer_200 = preprocessing.count_vectorizer_word_amount(merged_labeled_data, vocabulary, 200)
    print("    Count vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", count_vectorizer_200))
    print("    Count vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", count_vectorizer_200))
    tf_idf_200 = preprocessing.tf_idf(count_vectorizer_200)
    print("    TF-IDF vectorization, 10% test data:", average_classifier(classifier_function_name+"(test_data, 0.1)", tf_idf_200))
    print("    TF-IDF vectorization, 20% test data:", average_classifier(classifier_function_name+"(test_data, 0.2)", tf_idf_200))

    # Original data testing

    #for item in merged_labeled_data:
        #print(item[0])