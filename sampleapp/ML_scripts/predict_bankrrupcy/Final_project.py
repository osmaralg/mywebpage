

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.metrics import f1_score
from sklearn.utils import resample
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from style_functions import *


#credits https://towardsdatascience.com/predicting-bankruptcy-f4611afe8d2c

d =pd.read_csv("bankruptcy.csv")
#d = d.iloc[:, :-1]
cols = pd.read_csv("ColumnNames.csv")
#cols = cols.iloc[:, :]
#d.columns = cols.columns
label_column = "class"
d[label_column].replace("b'0'", 0b0, inplace=True)
d[label_column].replace("b'1'", 0b1, inplace=True)
d.replace("?", np.nan, inplace=True)
d.replace(r'', np.nan, inplace=True)
d = d.replace(r'^\s+$', np.nan, regex=True)
#d = (d.drop(cols.columns, axis=1).join(d.apply(pd.to_numeric, errors='coerce')))
d = d.astype(float)
feature_columns = [c for c in d.columns if c != label_column]


X = d[feature_columns].values
y = d[label_column].values
'''
from scipy import stats
z = (d - d.mean())/d.std(ddof=0)
print(z)
z_row = np.nanmax(z, axis=1)

X = X[z_row < 5]
y = y[z_row < 5]
'''
print("", X.shape)
#Pie chart
x = d['class'].value_counts()
labels = x
sizes = x
explode = (0, 0.2) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Pie chart showing imbalance in Dataset. \nOrange: Bankrupt , Blue: Not Bankrupt\n")

print(d.describe().T.style.render())
#d.style.apply(highlight_max, color='darkorange', axis=None)
describe_table = d.describe().T.style.apply(highlight_max, color='red', axis=0).render()
save_str_to_file(describe_table, 'machine_code.html')
# Showing only partial data


cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)

corr_map_str = d.corr()\
.style.background_gradient(cmap, axis=None)\
    .set_properties(**{'max-width': '80px', 'font-size': '1pt'})\
    .set_caption("Hover to magnify")\
    .set_precision(2)\
    .set_table_styles(magnify()).render()

save_str_to_file(corr_map_str, 'C:/Users/osmaralg/Desktop/mycompany/deploying-django-master/sampledeploy/sampleapp/templates/machine_corr_table.html')



imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp.fit(X)
X = imp.transform(X)

from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

print("Original feature size")
print("X.shape", X.shape)

select_features = 1
if select_features:
    lsvc = LinearSVC(penalty="l1", dual=False, C=0.0025, max_iter=10000).fit(X, y)
    model = SelectFromModel(lsvc, prefit=True)
    X = model.transform(X) # select only new features
    print("Feature size after regularization")
    print("X.shape", X.shape)


names = ["Logistic Regession with Lasso", "Logistic Regression with Ridge",
         "Logistic Regression Elastic Net", "KNeighbors Classifier",
         "Decision Tree", "AdaBoost"]

C = 0.7
classifiers = [
    LogisticRegression(multi_class='ovr', max_iter=5000000, solver='saga'),
    LogisticRegression(C=C, penalty='l2', tol=0.01, solver='saga'),
    LogisticRegression(C=C, penalty='elasticnet', solver='saga', l1_ratio=0.5, tol=0.01),
    KNeighborsClassifier(10),
    DecisionTreeClassifier(max_depth=200, class_weight='balanced'),
    AdaBoostClassifier()]

scores = []

#data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

clf = LogisticRegression().fit(X_train,y_train)
y_pred = clf.predict(X_test)

# Model Evaluation metrics
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score

print('Accuracy Score : ' + str(accuracy_score(y_test,y_pred)))
print('Precision Score : ' + str(precision_score(y_test,y_pred)))
print('Recall Score : ' + str(recall_score(y_test,y_pred)))
print('F1 Score : ' + str(f1_score(y_test,y_pred)))

#Logistic Regression Classifier Confusion matrix
from sklearn.metrics import confusion_matrix
print('Confusion Matrix : \n' + str(confusion_matrix(y_test,y_pred)))
from sklearn.model_selection import GridSearchCV
clf = LogisticRegression(max_iter=500000, solver='saga')
grid_values = {'penalty': ['l1', 'l2'], 'C':[0.01,.09,1,5,9,10,11,25]}
grid_clf_acc = GridSearchCV(clf, param_grid = grid_values,scoring = 'recall')
grid_clf_acc.fit(X_train, y_train)

#Predict values based on new parameters
y_pred_acc = grid_clf_acc.predict(X_test)

# New Model Evaluation metrics
print('Accuracy Score : ' + str(accuracy_score(y_test,y_pred_acc)))
print('Precision Score : ' + str(precision_score(y_test,y_pred_acc)))
print('Recall Score : ' + str(recall_score(y_test,y_pred_acc)))
print('F1 Score : ' + str(f1_score(y_test,y_pred_acc)))

#Logistic Regression (Grid Search) Confusion matrix
confusion_matrix(y_test,y_pred_acc)







model = make_pipeline(
    StandardScaler(), 
    AdaBoostClassifier()
).fit(X,y)

