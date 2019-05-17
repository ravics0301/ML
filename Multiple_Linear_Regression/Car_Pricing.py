import pandas as pd
import numpy as np 

data_set = pd.read_csv("/home/agl173/Passport/Untitled_Folder/Simple_L_3/CarPrice_Assignment.csv")
type(data_set)
X = data_set.iloc[:,[1,9,10,11,12,13,16,18,19,20,21,22,23]].values
Y = data_set.iloc[:,25].values

#make test and train data test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size  = 0.3)

# scale the data because datas are not in good format 
from sklearn.preprocessing import StandardScaler
stnd_scaler = StandardScaler()
X_stnd_scaler_Train = stnd_scaler.fit_transform(X_train)
X_stnd_scaler_Test = stnd_scaler.transform(X_test)

#applying linearRegression

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,Y_train)
Y_pred = lr.predict(X_test)

print(lr.coef_)
print(lr.intercept_)

#checking aquracy
from sklearn.metrics import r2_score
print(r2_score(Y_test,Y_pred))

Y_test.size

import matplotlib.pyplot as plt
plt.scatter(X_test[:,[2]],Y_test,c = 'red')
plt.plot(lr.predict(X_test),c = 'blue')
plt.show()

type(X)
