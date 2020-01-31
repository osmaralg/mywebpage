

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

def highlight_max(data, color='yellow'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)
#credits https://towardsdatascience.com/predicting-bankruptcy-f4611afe8d2c

d =pd.read_csv("bankruptcy_1.csv")
#d = d.iloc[:, :-1]
cols = pd.read_csv("ColumnNames.csv")
#cols = cols.iloc[:, :]
d.columns = cols.columns
label_column = "class"
d[label_column].replace("b'0'", 0b0, inplace=True)
d[label_column].replace("b'1'", 0b1, inplace=True)
d.replace("?", np.nan, inplace=True)
d.replace(r'', np.nan, inplace=True)
d = d.replace(r'^\s+$', np.nan, regex=True)
d = (d.drop(cols.columns, axis=1).join(d.apply(pd.to_numeric, errors='coerce')))
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
with open("describe_table.html", "w") as text_file:
    text_file.write(describe_table)
# Showing only partil data
sns.pairplot(d.iloc[0:10, 0:10])


imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp.fit(X)
X = imp.transform(X)

from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

print("Original feature size")
print("X.shape", X.shape)

select_features = 0
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
# Separate majority and minority classe
from sklearn.utils import resample
resampling = 0
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

if resampling:
    y_train = y_train.reshape(len(y_train),1)
    data = np.concatenate((X_train, y_train), axis=1)
    df_minority = data[data[:,-1] == 1]
    df_mayority = data[data[:,-1] == 0]

    print("mayority class size", df_mayority.size)
    print("minority class size", df_minority.size)

    df_minority_upsampled = resample(df_minority,
                                     replace=True,     # sample with replacement
                                     n_samples=np.shape(df_mayority)[0],    # to match majority class
                                     random_state=123) # reproducible results

    print("upsample size", df_minority_upsampled.shape)
    print("X_train original size", X_train.shape)
    X_train = np.concatenate((df_mayority[:,0:-1], df_minority_upsampled[:,0:-1]))
    y_train = np.concatenate((df_mayority[:, -1], df_minority_upsampled[:,-1]))

    y_train = y_train.reshape(len(y_train),1)
    data = np.concatenate((X_train, y_train), axis=1)
    df_minority = data[data[:,-1] == 1]
    df_mayority = data[data[:,-1] == 0]

    print("mayority class size", df_mayority.size)
    print("minority class size", df_minority.size)

    df_minority_upsampled = resample(df_minority,
                                     replace=True,     # sample with replacement
                                     n_samples=np.shape(df_mayority)[0],    # to match majority class
                                     random_state=123) # reproducible results

    print("upsample size", df_minority_upsampled.shape)
    print("X_train original size", X_train.shape)
    X_train = np.concatenate((df_mayority[:,0:-1], df_minority_upsampled[:,0:-1]))
    y_train = np.concatenate((df_mayority[:, -1], df_minority_upsampled[:,-1]))

    print("x train size", X_train.shape)
    print("y_train_size", y_train.shape)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, max_iter=10000,
                    hidden_layer_sizes=(65, 5), random_state=1)
model = clf.fit(X_train, y_train)
print(model)
print("F1 score: ", round(f1_score(y_test, model.predict(X_test)), 4))
print(model.predict(X_test))

fig, ax = plt.subplots(figsize=(8, 8))
for name, clf in zip(names, classifiers):
    print("Training " , name + '...')
    model = make_pipeline(
        clf).fit(X_train, y_train)
    fprs, tprs, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
    roc_score = round(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]),4)
    ax.plot(fprs, tprs, label=name + " " + str(roc_score))
    ax.set_xlabel('False positive rate')
    ax.set_ylabel('True positive rate')
    ax.set_title(r"All models with thresholds $0, 0.05, 0.1, \ldots, 0.95, 1.0$");
    ax.legend()
    print(name + " ROC_AUC_SCORE :", roc_score)
    print("F1 score: ", round(f1_score(y_test, model.predict(X_test)),4)) 
    print("Recall: ", round(recall_score(y_test, model.predict(X_test)),4)) 
    print("Precision: ", round(precision_score(y_test, model.predict(X_test)),4)) 
    print("------------------------------------------------------")

plt.show()
# # Model Selection

# From above, we can see that most of the models have a good F1 score. However, the models with the top ROC-AUC score are AdaBoost and Random Forest. To decide the best between them, we perform K-Fold Cross Validation on these two models. In k-fold cross valdidation we take k = 10. We calculate both F1 score and ROC-AUC using the command cross_val_score. We chose the final model based only on the F1 score as our data is unbalanced. 

# In[ ]:


names = ["Decision Tree", "AdaBoost"]

classifiers = [
    DecisionTreeClassifier(max_depth=500, class_weight='balanced'),
    AdaBoostClassifier()]

scores = ['f1' , 'roc_auc', 'f1_micro']

#data split

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

kfold = KFold(n_splits = 10, shuffle = True, random_state = 3)
print("Cross Validation")
for name, clf in zip(names, classifiers):
    print("Training " , name + '...')
    for score in scores:
        Model_scores = cross_val_score(clf, X_train, y_train, scoring = score, cv = kfold)
        avg = round(np.mean(Model_scores),4)
        print("Scores: ", score , avg)
    print('----------------------------------------------------')


# The best model is Adaboost. We evaulate the performance of the the winner model over the test set.

# In[ ]:


model = make_pipeline(
    StandardScaler(), 
    AdaBoostClassifier()
).fit(X_train, y_train)

from sklearn import preprocessing
#scaler = preprocessing.StandardScaler().fit(X_train)
#X_test = scaler.transform(X_test)
print("Recall: ", round(recall_score(y_test, model.predict(X_test)),4))
print("Precision: ", round(precision_score(y_test, model.predict(X_test)),4))
print("F1 score: ", round(f1_score(y_test, model.predict(X_test)),4))
print("ROC-AUC: ", round(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]),4))
matrix = confusion_matrix(y_test, model.predict(X_test))
print(matrix)


# # Retrain the model with all data
# In our final step, we train on the entire dataset with the winner model - Adaboost. This model is ready for production after re-training.  

# In[ ]:


model = make_pipeline(
    StandardScaler(), 
    AdaBoostClassifier()
).fit(X,y)

