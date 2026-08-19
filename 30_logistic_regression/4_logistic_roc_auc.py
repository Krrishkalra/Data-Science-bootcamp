from matplotlib import pyplot
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X,y = make_classification(n_samples=10000, n_features=2,n_clusters_per_class=1, n_redundant=0, weights=[0.99], random_state=10)

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

dummy_model_prob = [0 for _ in range(len(y_test))]

model = LogisticRegression()
model.fit(X_train,y_train)

model_prob = model.predict_proba(X_test)
model_prob = model_prob [:,1]

dummy_model_auc = roc_auc_score(y_test,dummy_model_prob)
model_auc = roc_auc_score(y_test,model_prob)

## false positive rate and true positive rate is what we get from the roc_auc scores

## And if we plot tpr on the y axis and fpr on the x axis we would get the roc curve

dummy_fpr, dummy_tpr, _ = roc_curve(y_test, dummy_model_prob)
model_fpr, model_tpr, _ = roc_curve(y_test, model_prob)

pyplot.plot(dummy_fpr, dummy_tpr, linestyle='--', label='Dummy model')
pyplot.plot(model_fpr, model_tpr, marker='.', label='logistic')

pyplot.xlabel('False Positive rate(FPR)')
pyplot.ylabel('True Positive rate(TPR)')
pyplot.legend()
pyplot.show()