from __future__ import print_function
import numpy as np
from sklearn import datasets,linear_model
#height(cm), input data, each row is a data point
X=np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
#weight (kg)
y=np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])
#Building Xbar
one=np.ones((X.shape[0],1))
#each row is one data point
Xbar=np.concatenate((one,X),axis=1)
Trang 84/84
#Calculating weights of the linear regression model
A=np.dot(Xbar.T,Xbar)
b=np.dot(Xbar.T,y)
w=np.dot(np.linalg.pinv(A),b)
#fit the model by Linear Regression
regr=linear_model.LinearRegression()
#in scikit-learn, each sample is one row
regr.fit(X,y)
#Compare two results
print("scikit-lean's solution:w_1=",regr.coef_[0],"w_0=",regr.intercept_)
print("our solution : w_1 = ",w[1],"w_0=",w[0])
yourHeight=int(input("Input your height:"))
yourWeight=regr.coef_[0]*yourHeight+regr.intercept_
print("Your height is ",yourHeight,", I predict your weight is
",yourWeight,"kg")
Chạy phần mềm ta được:
scikit-lean's solution:w_1= 0.5592049619396674 w_0= -33.73541020580774
our solution : w_1 = 0.5592049619425978 w_0= -33.735410206296365
Input your height:>? 170
Your height is 170 , I predict your weight is 61.32943332393572 kg
