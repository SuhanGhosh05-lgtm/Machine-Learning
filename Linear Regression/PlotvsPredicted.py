import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data={'Experience':[1,2,3,4,5],
      'Salary':[25000,40000,80000,120000,150000]}
df=pd.DataFrame(data)
print(df)

#double brackets create data frame of 2D
x=df[['Experience']] #features:- in the model we use all these datas in x to learn these features and make predictions
y=df['Salary'] #target

# x_train	Input values used to train the model	6
# y_train	Actual output values for training	6
# x_test	Input values used to test the model	2
# y_test	Actual output values for testing	2

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print(y_pred)

print("Actual salary:", y_test.values)
print("Predicted salary:", y_pred)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred)) #total avg of all of the ssquared errors=sqroot((x2-x1)^2+(y2-y1)^2)
print("R2 Score:", r2_score(y_test, y_pred))

#plotting actual vs predicted data
# Predict for all experience values
y_all_pred = model.predict(x)

# Actual data points
plt.scatter(x['Experience'], y, color='blue', label='Actual')

# Predicted regression line
plt.plot(x['Experience'], y_all_pred, color='red', marker='o', label='Predicted')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.title('Experience vs Salary')
plt.legend()
plt.grid(True)
plt.show()
