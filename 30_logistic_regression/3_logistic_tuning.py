import warnings
warnings.filterwarnings('ignore')

from collections import Counter
from sklearn.datasets import make_classification

X,y = make_classification(n_samples=10000, n_features=2,n_clusters_per_class=1, n_redundant=0, weights=[0.99], random_state=10)

import seaborn as sns
import pandas as pd
sns.scatterplot(x=pd.DataFrame(X)[0], y=pd.DataFrame(X)[1], hue=y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
penalty = ['l1','l2','elasticnet']
solver = ['newton-cg','lbfgs','liblinear','sag','saga']
c_values = [100,10,1,0.1,0.01]
class_weight = [{0:w,1:y} for w in [1,10,50,100] for y in [1,10,50,100]]

params = dict(penalty=penalty, C=c_values, solver=solver, class_weight=class_weight)

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV

cv = StratifiedKFold()

grid = GridSearchCV(estimator=model, param_grid=params, scoring='accuracy',n_jobs=1,cv=cv)

grid.fit(X_train,y_train)
print(grid.best_params_)
print(grid.best_score_)

print('\n')
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
y_pred = grid.predict(X_test)
print(accuracy_score(y_pred, y_test))
print(classification_report(y_pred, y_test))
print(confusion_matrix(y_pred, y_test))