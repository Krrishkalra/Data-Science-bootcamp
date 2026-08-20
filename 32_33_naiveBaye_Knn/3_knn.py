## K nearest neighbor
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification

X,y = make_classification(n_samples=1000,n_features=3,n_redundant=1,n_classes=2,random_state=999)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=42)

from sklearn.neighbors import KNeighborsClassifier

knc = KNeighborsClassifier(n_neighbors=5,algorithm='auto')
knc.fit(X_train,y_train)
y_pred = knc.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
print("before gridsearch")
print(confusion_matrix(y_pred,y_test))
print(accuracy_score(y_pred,y_test))
print(classification_report(y_pred,y_test))

## perform GridSearchCV on this dataset with k=1,2,3,4,5,6,7,8,9,10
from sklearn.model_selection import GridSearchCV

params = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
grid = GridSearchCV(KNeighborsClassifier(), param_grid=params, cv=5)
grid.fit(X_train, y_train)
print("Best parameters:", grid.best_params_)
print("Best score:", grid.best_score_)

y_pred = grid.predict(X_test)
print("after gridsearch")
print(y_pred)
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

# also perform KNeighborRegressor with the same method 

from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor

X1,y1 = make_regression(n_samples=1000,n_features=3,n_informative=2,random_state=999)
X1_train,X1_test,y1_train,y1_test = train_test_split(X1,y1,test_size=0.30,random_state=42)

knr = KNeighborsRegressor(n_neighbors=5,algorithm='auto')
knr.fit(X1_train,y1_train)
y1_pred = knr.predict(X1_test)
from sklearn.metrics import mean_squared_error, r2_score
print("r2",r2_score(y1_test,y1_pred))
print("MSE",mean_squared_error(y1_test,y1_pred))