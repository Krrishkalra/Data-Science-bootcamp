#Support vector regression

#tips dataset
import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
df = sns.load_dataset('tips')
df.head()

#total bill is the dependent feature which we will try to predict using SVM

df['sex'].value_counts()

df['smoker'].value_counts()

df['day'].value_counts()

df['time'].value_counts()

## now we will implement label encoding and one hot encoding because all the features generally have specific values 2(label) or more (one hot)

X = df[['tip', 'sex', 'smoker', 'day', 'time', 'size']]
y = df['total_bill']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

#Feature encoding
from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()

X_train['sex']=le1.fit_transform(X_train['sex'])
X_train['smoker']=le2.fit_transform(X_train['smoker'])
X_train['time']=le3.fit_transform(X_train['time'])

X_train.head()

X_test['sex']=le1.transform(X_test['sex'])
X_test['smoker']=le2.transform(X_test['smoker'])
X_test['time']=le3.transform(X_test['time'])

X_test.head()


## onehot encoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(
    transformers=[('onehot', OneHotEncoder(drop='first', sparse_output=False), [3])],
    remainder='passthrough'
)

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
X_train = np.asarray(ct.fit_transform(X_train), dtype=float)
X_test = np.asarray(ct.transform(X_test), dtype=float)


### SVR mplementation
from sklearn.svm import SVR
svr= SVR()

svr.fit(X_train,y_train)
y_pred = svr.predict(X_test)

from sklearn.metrics import r2_score, mean_absolute_error
print(r2_score(y_test,y_pred))
print(mean_absolute_error(y_test, y_pred))

### hyperparameter tuning using gridsearch

from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1,1,10,100,100],
'gamma':[1,0.1,0.01,0.001,0.001],
'kernel':['rbf'] }

grid = GridSearchCV(SVR(),param_grid, refit=True,cv=5)
grid.fit(X_train,y_train)

y_pred_grid = grid.predict(X_test)

from sklearn.metrics import r2_score, mean_absolute_error
print(r2_score(y_test,y_pred_grid))
print(mean_absolute_error(y_test, y_pred_grid))