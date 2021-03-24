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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=percentage, random_state=0)
    return X_train, X_test, y_train, y_test