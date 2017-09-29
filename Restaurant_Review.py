import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

nltk.download('stopwords')

corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

classifierNB = GaussianNB()
classifierNB.fit(X_train, y_train)
y_pred = classifierNB.predict(X_test)
cmNB = confusion_matrix(y_test, y_pred)

from sklearn.tree import DecisionTreeClassifier
classifierDT = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifierDT.fit(X_train, y_train)
y_pred = classifierDT.predict(X_test)
cmDT = confusion_matrix(y_test, y_pred)

from sklearn.ensemble import RandomForestClassifier
classifierRF = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifierRF.fit(X_train, y_train)
y_pred = classifierRF.predict(X_test)
cmRF = confusion_matrix(y_test, y_pred)

from sklearn.linear_model import LogisticRegression
classifierLR = LogisticRegression(random_state = 0)
classifierLR.fit(X_train, y_train)
y_pred = classifierLR.predict(X_test)
cmLR = confusion_matrix(y_test, y_pred)

from sklearn.neighbors import KNeighborsClassifier
classifierKN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifierKN.fit(X_train, y_train)
y_pred = classifierKN.predict(X_test)
cmKN = confusion_matrix(y_test, y_pred)

from sklearn.svm import SVC
classifierSVM = SVC(kernel = 'linear', random_state = 0)
classifierSVM.fit(X_train, y_train)
y_pred = classifierSVM.predict(X_test)
cmSVM = confusion_matrix(y_test, y_pred)

classifierSVMrbf = SVC(kernel = 'rbf', random_state = 0)
classifierSVMrbf.fit(X_train, y_train)
y_pred = classifierSVMrbf.predict(X_test)
cmSVMrbf = confusion_matrix(y_test, y_pred)
