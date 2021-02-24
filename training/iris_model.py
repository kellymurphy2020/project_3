from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import numpy as np


def train(X,y):
    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    knn = KNeighborsClassifier(n_neighbors=1)

    # fit the model
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f'Model accuracy on test set: {acc:.2f}')
    return knn

if __name__ == '__main__':
    # Load IRIS data
    iris_data = datasets.load_iris()
    X = iris_data['data']
    y = iris_data['target']

    labels = {0 : 'iris-setosa',
              1 : 'iris-versicolor',
              2 : 'iris-virginica'}

    # Different way to vectorize labels
    y = np.vectorize(labels.__getitem__)(y)

    model = train(X,y)

    # serialize model
    joblib.dump(model, '../iris.smd')
    print("Model is saved.")
