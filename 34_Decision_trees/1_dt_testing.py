import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris_data, iris_target = load_iris(return_X_y=True)

# independent
X = pd.DataFrame(iris_data, columns=['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm'])

# dependent
y = iris_target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=10)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
y_pred = dtc.predict(X_test)
#VISUALIZE

from sklearn import tree
plt.figure(figsize=(15,10))
print(tree.plot_tree(dtc,filled=True))
plt.show()

from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
print("without post pruning")
print(confusion_matrix(y_pred,y_test))
print(accuracy_score(y_pred,y_test))
print(classification_report(y_pred,y_test))

## 2ND DTC for POST PRUNNING

dtc2 = DecisionTreeClassifier(max_depth=2)
dtc2.fit(X_train,y_train)

from sklearn import tree
plt.figure(figsize=(15,10))
print(tree.plot_tree(dtc2,filled=True))
plt.show()

y_pred2 = dtc2.predict(X_test)
print("with post pruning")
print(confusion_matrix(y_pred2,y_test))
print(accuracy_score(y_pred2,y_test))
print(classification_report(y_pred2,y_test))

# -----------------------------------

### Pre pruning and hyperparameter tuning

param = {'criterion':['gini','entropy', 'log_loss'],'splitter':['best','random'],'max_depth':[1,2,3,4,5],'max_features':['auto','sqrt','log2']}
from sklearn.model_selection import GridSearchCV

grid_dtc = GridSearchCV(dtc,param_grid=param,cv=5,scoring='accuracy')
grid_dtc.fit(X_train,y_train)

print(grid_dtc.best_params_)
print(grid_dtc.best_score_)

y_pred_new = grid_dtc.predict(X_test)
print(accuracy_score(y_test,y_pred_new))
print(confusion_matrix(y_test,y_pred_new))
print(classification_report(y_test,y_pred_new))