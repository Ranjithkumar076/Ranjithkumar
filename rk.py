# -*- coding: utf-8 -*-
"""Rk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J_lUP-KvyaNtDijwu8c7s2AaX8inL7zX
"""

import pandas as pd

import numpy as np

import pickle

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import seaborn as sns

import sklearn

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.model_selection import RandomizedSearchCV

import imblearn

from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix,f1_score

#import dataset
data = pd.read_csv(r"/content/Churn_Modelling.csv")

data.info()

data.RowNumber = pd.to_numeric(data.RowNumber, errors ='coerce')
data.isnull().any()

data["Age"].fillna(data["Age"].median(), inplace =True)
data.isnull().sum()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["RowNumber"] = le.fit_transform(data["RowNumber"])
data["CustomerId"] = le.fit_transform(data["CustomerId"])
data["Surname"] = le.fit_transform(data["Surname"])
data["CreditScore"] = le.fit_transform(data["CreditScore"])
data["Geography"] = le.fit_transform(data["Geography"])
data["Gender"] = le.fit_transform(data["Gender"])
data["Age"] = le.fit_transform(data["Age"])
data["Tenure"] = le.fit_transform(data["Tenure"])
data["Balance"] = le.fit_transform(data["Balance"])
data["NumOfProducts"] = le.fit_transform(data["NumOfProducts"])
data["HasCrCard"] = le.fit_transform(data["HasCrCard"])
data["IsActiveMember"] = le.fit_transform(data["IsActiveMember"])
data["EstimatedSalary"] = le.fit_transform(data["EstimatedSalary"])
data["Exited"] = le.fit_transform(data["Exited"])

data.head()

x=data.iloc[:,0:19].values
y=data.iloc[:,19:20].values

x

y

from sklearn.preprocessing import OneHotEncoder
one = OneHotEncoder()
a= one.fit_transform(x[:,6:7]).toarray()
b= one.fit_transform(x[:,7:8]).toarray()
c= one.fit_transform(x[:,8:9]).toarray()
d= one.fit_transform(x[:,9:10]).toarray()
e= one.fit_transform(x[:,10:11]).toarray()
f= one.fit_transform(x[:,11:12]).toarray()
g= one.fit_transform(x[:,12:13]).toarray()
y= one.fit_transform(x[:,13:14]).toarray()
x=np.delete(x,[6,7,8,9,10,11,12,13,],axis=1)
x=np.concatenate((a,b,c,d,e,f,g,y,x),axis=1)

from imblearn.over_sampling import SMOTE

smt = SMOTE()

x_resample, y_resample = smt.fit_resample(x,y)

x_resample

y_resample

x.shape,y_resample.shape

y.shape,y_resample.shape

data.describe()

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.distplot(data["Tenure"])
plt.subplot(1,2,2)
sns.distplot(data["HasCrCard"])

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.countplot(data["Gender"])
plt.subplot(1,2,2)
sns.countplot(data["Balance"])

sns.barplot(x="Gender",y="Balance",data=data)

sns.heatmap(data.corr(), annot=True)

sns.pairplot(data=data, markers=["^","v"], palette="inferno")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_resample,y_resample,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

x_train.shape

#importing and building the log reg model 
def logreg(x_train,x_test,y_train,y_test):
   lr = LogisticRegression (random_state=0)
   lr.fit(x_train,y_train)
   y_lr_tr = lr.predict(x_train)
   print(accuracy_score(y_lr_tr,y_train)) 
   yPred_lr = lr.predict(x_test) 
   print(accuracy_score (yPred_lr,y_test)) 
   print("***Logistic Regression***") 
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_lr))
   print("Classification Report")
   print(classification_report(y_test,yPred_lr))

logreg(x_train,x_test,y_train,y_test)

#importing and building the Decision tree model 
def decisionTree(x_train,x_test,y_train,y_test):
   dtc = DecisionTreeClassifier(criterion="entropy",random_state=0)
   dtc.fit(x_train,y_train)
   y_dt_tr = dtc.predict(x_train)
   print(accuracy_score(y_dt_tr,y_train)) 
   yPred_dt = dtc.predict(x_test) 
   print(accuracy_score (yPred_dt,y_test)) 
   print("***Decision Tree***") 
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_dt))
   print("Classification Report")
   print(classification_report(y_test,yPred_dt))

decisionTree(x_train,x_test,y_train,y_test)

#importing and building the random forest model 
def RandomForest(x_train,x_test,y_train,y_test):
   rf = RandomForestClassifier(criterion="entropy",random_state=0)
   rf.fit(x_train,y_train)
   y_rf_tr = rf.predict(x_train)
   print(accuracy_score(y_rf_tr,y_train)) 
   yPred_rf = rf.predict(x_test) 
   print(accuracy_score (yPred_rf,y_test)) 
   print("***Random Forest***") 
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_rf))
   print("Classification Report")
   print(classification_report(y_test,yPred_rf))

RandomForest(x_train,x_test,y_train,y_test)

#importing and building the KNN model 
def KNN(x_train,x_test,y_train,y_test):
   knn = KNeighborsClassifier()
   knn.fit(x_train,y_train)
   y_knn_tr = knn.predict(x_train)
   print(accuracy_score(y_knn_tr,y_train)) 
   yPred_knn = knn.predict(x_test) 
   print(accuracy_score (yPred_knn,y_test)) 
   print("***KNN***") 
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_knn))
   print("Classification Report")
   print(classification_report(y_test,yPred_knn))

KNN(x_train,x_test,y_train,y_test)

#importing and building the random forest model 
def svm(x_train,x_test,y_train,y_test):
   svm = SVC(kernel = "linear")
   svm.fit(x_train,y_train)
   y_svm_tr = svm.predict(x_train)
   print(accuracy_score(y_svm_tr,y_train)) 
   yPred_svm = svm.predict(x_test) 
   print(accuracy_score (yPred_svm,y_test)) 
   print("***Support Vector Machine***") 
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_svm))
   print("Classification Report")
   print(classification_report(y_test,yPred_svm))

svm(x_train,x_test,y_train,y_test)

import keras 
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units=30,activation='relu',input_dim=40))

classifier.add(Dense(units=30,activation='relu'))

classifier.add(Dense(units=30,activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crosssentrophy',metrics=['accuracy'])

model_history = classifier.fit(x_train,y_train,batch_size=10,validation_split=0.33, epochs=200)

ann_pred = classifier.predict(x_test)
ann_pred = (ann_pred>0.5)
ann_pred

print(accuracy_score(ann_pred,y_test))
print("***ANN Model***")
print("Confusion_Matrix")
print(confusion_matrix(y_test,ann_pred))
print("Classification Report")
print(classification_report(y_test,ann_pred))

lr = LogisticRegression(random_state=0)
lr.fit(x_train,y_train)
print("predicting on random input")
lr_pred_own = lr.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",lr_pred_own)

dtc = DecisionTreeClassifier(criterion="entrophy",random_state=0)
dtc.fit(x_train,y_train)
print("Predicting on random input")
dtc_pred_own = dtc.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",dtc_pred_own)

rf = RandomForestClassifier(criterion="entrophy",n_estimators=10,random_State=0)
rf.fit(x_train,y_train)
print("Predicting on random input")
rf_pred_own = rf.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",rf_pred_own)

svc = SVC(kernel = "linear")
svc.fit(x_train,y_train)
print("predicting in random input")
svm_pred_own = svc.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",svm_pred_own)

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print("predicting on random input")
knn_pred_own = knn.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",knn_pred_own)

print("predicting on random input")
ann_pred_own = classifier.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print(ann_pred_own)
ann_pred_own = (ann_pred_own>0.5)
print("output is: ",ann_pred_own)

def compareModel(X_train,X_test,y_train,y_test):
  logreg(X_train,X_test,y_train,y_test)
  print('_'*100)
  decisionTree(X_train,X_test,y_train,y_test)
  print('_'*100)
  RandomForest(X_train,X_test,y_train,y_test)
  print('_'*100)
  svm(X_train,X_test,y_train,y_test)
  print('_'*100)
  KNN(X_train,X_test,y_train,y_test)
  print('_'*100)

comparteMode;l(X_train,X_test,y_train,y_test)

classifier .save("telcom_churn.hs")

from flask import flask, render_template, request 
import keras
from keras.models import load_model

app = Flask(__name__)
model = load_model("telecom_churn.h5")

@app.route('/')
def home();
  return render_template('home.html')

@app.route('/')
def helloworld():
  return render_template("base.html")
@app.route('/assesment')
def prediction():
  return render_template("index.html")
@app.route('/predict', methods = ['POST'])
def admin():
  a  = request.form["gender"]
  if (a=='f'):
      a=0
  if (a=='m'):
      a=1
  b= request.form["srcitizen"]
  if (b == 'n'):
      b=0
  if (b=='y'):
      b=1
  c= request.form["partner"]
  if (c=='n'):
      c=0
  if (c=='y'):
      c=1
  d= request.form["dependents"]
  if (d== 'n'):
    d=0
  if (d== 'y'):
    d=1
  e= request.form["tenure"]
  f= request.form["phservices"]
  if (f=='n'):
      f=0
  if (f=='y'):
      f=1
  g= request.form["multi"]
  if (g=='n'):
      g1,g2,g3=1,0,0
  if (g=='nps'):
      g1,g2,g3=0,1,0
  if (g=='y'):
      g1,g2,g3=0,0,1
  h= request.form["is"]
  if (h == 'dsl'):
    h1,h2,h3=1,0,0
  if(h == 'fo'):
    h1,h2,h3=0,1,0
  if(h == 'n'):
    h1,h2,h3=0,0,1
  i= request.form["os"]
  if (i == 'n'):
    i1,i2,i3=1,0,0
  if(i == 'nis'):
    i1,i2,i3=0,1,0
  if(i == 'y'):
    i1,i2,i3=0,0,1
  j= request.form["ob"]
  if (j == 'n'):
    j1,j2,j3=1,0,0
  if (j == 'y'):
    j1,j2,j3=0,0,1
  k= request.form["dp"]
  if (k== 'n'):
    k1,k2,k3=1,0,0
  if(k == 'nis'):
    k1,k2,k3=0,0,1
  l= request.form["ts"]
  if (l == 'n'):
    l1,l2,l3=1,0,0
  if (l == 'nis'):
    l1,l2,l3=0,1,0
  if (l == 'y'):
    l1,l2,l3=0,0,1
  m= request.form["stv"]
  if (m == 'n'):
    m1,m2,m3=1,0,0
  if (m == 'nis'):
    m1,m2,m3=0,1,0
  if (m == 'y'):
    m1,m2,m3=0,0,1
  n= request.form["smv"]
  if (n == 'n'):
    n1,n2,n3=1,0,0
  if (n == 'nis'):
    n1,n2,n3=0,1,0
  if (n == 'y'):
    n1,n2,n3=0,0,1
  o= request.form["contract"]
  if (o == 'mtm'):
    o1,o2,o3=1,0,0
  if (o == 'oyr'):
    o1,o2,o3=0,1,0
  if (o == 'tyrs'):
    o1,o2,o3=0,0,1
  p= request.form["pmt"]
  if (p == 'ec'):
    p1,p2,p3,p4=1,0,0,0
  if (p == 'mail'):
    p1,p2,p3,p4=0,1,0,0
  if (p == 'bt'):
    p1,p2,p3,p4=0,0,1,0
  if (p == 'cc'):
    p1,p2,p3,p4=0,0,0,1
  q= request.form["plb"]
  if (q == 'n'):
      q=0
  if (q == 'y'):
      q=1
  r= request.form["mcharges"]
  s= request.form["tcharges"]

  t=[[int(g1),int(g2),int(g3),int(h1),int(h2),int(h3),int(i1),int(i2),int(i3),int(j1),int(j2),int(j3)]]
  print(t)
  x = model.predict(t)
  print(x[0])
  if (x[[0]]<=0.5):
      y ="No"
      return render_template("predno.html",z = y)
  
  if (x[[0]] >= 0.5):
    y ="Yes"
    return render_template("predyes.html", z = y)



