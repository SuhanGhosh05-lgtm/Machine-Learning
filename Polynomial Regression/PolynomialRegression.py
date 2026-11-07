from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([1.2,1.6,1.9,2.3,3.7])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

poly = PolynomialFeatures(degree=2)
# x_train_poly: the transformed inputs.
# y_train: the correct outputs corresponding to those inputs.
x_train_poly = poly.fit_transform(x_train) #fits the data accordingly
x_test_poly = poly.transform(x_test) #works on the fitted data

model = LinearRegression()
model.fit(x_train_poly, y_train)

pred = model.predict(x_test_poly)

print("R2 Score:", r2_score(y_test, pred))

# x         	All input values
# y         	All actual output values
# x_train	    Input values used to train the model
# x_test	    Input values reserved for testing
# y_train	    Actual outputs corresponding to training inputs
# y_test	    Actual outputs corresponding to test inputs
# poly	        Object that creates polynomial features
# x_train_poly	Training inputs converted into polynomial features
# x_test_poly	Test inputs converted into polynomial features
# model	        Linear Regression model that learns the equation
# pred	        Predictions made by the trained model