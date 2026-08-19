# support vector machine

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# synthetic data points
from sklearn.datasets import make_classification

X,y = make_classification(n_samples=1000,n_features=2,n_classes=2,n_clusters_per_class=1,n_redundant=0)

sns.scatterplot(x=pd.DataFrame(X)[0],y=pd.DataFrame(X)[1],hue=y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)

from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))



# data not linearly separable

X,y = make_classification(n_samples=1000,n_features=2,n_classes=2,n_clusters_per_class=2,n_redundant=0)

sns.scatterplot(x=pd.DataFrame(X)[0],y=pd.DataFrame(X)[1],hue=y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)

from sklearn.svm import SVC
rbf = SVC(kernel='rbf')
rbf.fit(X_train,y_train)

y_pred_new = rbf.predict(X_test)
print(classification_report(y_test,y_pred_new))
print(confusion_matrix(y_test,y_pred_new))


from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1,1,10,100,1000],'gamma': [1,0.1,0.01,0.001,0.0001],'kernel':['rbf']}

grid = GridSearchCV(SVC(),param_grid=param_grid,refit=True,cv=5,verbose=3)
grid.fit(X_train,y_train)
y_pred_grid = grid.predict(X_test)
print(classification_report(y_test,y_pred_grid))
print(confusion_matrix(y_test,y_pred_grid))