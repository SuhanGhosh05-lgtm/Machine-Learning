import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

#loading the dataset
housing=fetch_california_housing()
df=pd.DataFrame(housing.data,
                 columns=housing.feature_names)
#adding the target variable
df['PRICE']=housing.target
#printing first 5 rows from the data
print(df.head())
#checking missing values
print(df.isnull().sum())

#independent variable vs dependent variable
x=df[['MedInc', 'HouseAge', 'AveRooms',
        'AveBedrms', 'Population', 'AveOccup',
        'Latitude', 'Longitude']]
y=df['PRICE']

#splitting the datas
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#training the data
model=LinearRegression()
model.fit(x_train,y_train)
#prediction
y_pred=model.predict(x_test)

print("R2_score:-",r2_score(y_test,y_pred))
print("MSE:-",mean_squared_error(y_test,y_pred))
print("RMSE:-",np.sqrt(mean_squared_error(y_test,y_pred)))

#plotting actual vs predicted data
plt.scatter(y_test,y_pred,alpha=0.3)
plt.xlabel("Actual house prices")
plt.ylabel("Predicted house prices")
plt.title("MLR: Actual vs Predicted")
#ideal prediction fit
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)
plt.show()