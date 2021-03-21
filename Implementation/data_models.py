from sklearn.model_selection import train_test_split


def split_data_by_articles():
    pass


def split_test_train_data(data, percentage):
    """ Split data into testing and training based on chosen percentage """
    y = [item[0] for item in data]
    X = [item[1] for item in data]
    # Get training and testing vectors in X, labels in y
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=percentage, random_state=0)
    return X_train, X_test, y_train, y_test