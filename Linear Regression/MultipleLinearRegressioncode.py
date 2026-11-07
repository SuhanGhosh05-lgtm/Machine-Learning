#                           Multiple Linear Regression:- 1 dependent predicted with many independent values
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

x = np.array([
    [1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
    [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]
])

y = np.array([2, 4, 6, 8, 9, 11, 13, 15, 17, 19])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

pred = model.predict(x_test)

print("Actual values:", y_test)
print("Predicted values:", pred)
print("R2 Score:", r2_score(y_test, pred))

