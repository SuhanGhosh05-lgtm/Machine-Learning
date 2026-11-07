import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

#loading boston data house set
housing=fetch_california_housing()
df=pd.DataFrame(housing.data,
                columns=housing.feature_names)

#Add the target variable (house prices) to the DataFrame
df['PRICE']=housing.target

## Display the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Define the feature (independent variable) and target (dependent variable)
x=df[['AveRooms']] #independent
y=df['PRICE'] #dependent

#splitting the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=24)
#train the model
model=LinearRegression()
model.fit(x_train,y_train)
#predict the price
y_pred=model.predict(x_test)
#evaluate the model
print('R2_SCORE=',r2_score(y_test,y_pred))
print("MSE:-",mean_squared_error(y_test,y_pred))

#plotting the results
plt.scatter(x_test['AveRooms'],y_test,label='Actual prices',color='blue',linewidths=5)
plt.scatter(x_test['AveRooms'],y_pred,label='Predicted price',color='red',linewidths=5)
plt.xlabel('Avg rooms')
plt.ylabel('Median House Value ($100,000 units)')
plt.legend()
plt.show()


