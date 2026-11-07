from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split #to distribute data into training and testing
from sklearn.metrics import r2_score #to evaluate a LR model, better score means model has worked well,less means improvement
import numpy as np
#                                                  size
# x_train	Input values used to train the model	6
# y_train	Actual output values for training	6
# x_test	Input values used to test the model	2
# y_test	Actual output values for testing	2
                                                #with a random data
x=np.array([[1],[2],[3],[8],[9],[6],[4],[5]])
y=np.array([1.3,4.8,3.9,8,4,3,5,1])

#test size=20%, remaining 80% for training, 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)

pred=model.predict(x_test)
print(r2_score(y_test,pred)) #-3.5782735756830837, it says, not directly correlated but inversely correlated

# pred = model.predict(x_test) predicts outputs for the test inputs.
# y_test contains the actual outputs for those same inputs.
# r2_score(y_test, pred) compares actual and predicted outputs to evaluate your model.

                                                #now with a cleaner data
a=np.array([[1],[2],[3],[8],[9],[10]])
b=np.array([1,4,6,16,18,20])

#test size=20%, remaining 80% for training, 
a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.2,random_state=10)
model=LinearRegression()
model.fit(a_train,b_train)

pred=model.predict(a_test)

print(r2_score(b_test,pred))