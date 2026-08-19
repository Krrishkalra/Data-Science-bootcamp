# svc using kernels 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import SVC

x = np.linspace(-5.0,5.0,100)
y = np.sqrt(10**2 - x**2)
y = np.hstack([y,-y])
x = np.hstack([x,-x])
print(y)

x1 = np.linspace(-5.0,5.0,100)
y1 = np.sqrt(5**2 - x1**2)
y1 = np.hstack([y1,-y1])
x1 = np.hstack([x1,-x1])
print(y1)

plt.scatter(y,x)
plt.scatter(y1,x1)

np.vstack([y,x]).T

import pandas as pd
df1 = pd.DataFrame(np.vstack([y,x]).T,columns=['X1','X2'])
df1['Y']=0
df2 = pd.DataFrame(np.vstack([y1,x1]).T,columns=['X1','X2'])
df2['Y']=1
df = pd.concat([df1, df2], ignore_index=True)
df.head()

df.tail()

X = df.iloc[:,:2]
y = df.Y

df['X1_sq'] = df['X1']**2
df['X2_sq'] = df['X2']**2
df['X1*X2'] = df['X1']*df['X2']

X = df[['X1','X2','X1_sq','X2_sq','X1*X2']]
y = df['Y']
df.head()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
print(y_train)

import plotly.express as px
fig = px.scatter_3d(df,x='X1',y='X2',z='X1*X2', color='Y')
fig.show()

fig = px.scatter_3d(df,x='X1_sq',y='X2_sq',z='X1*X2', color='Y')
fig.show()

classifier = SVC(kernel='linear')
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))