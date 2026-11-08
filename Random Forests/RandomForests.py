from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

x=np.array([[1],[2],[3],[4],[5],[6],[3],[4],[5],[6],[7],[8]])
y=np.array([1.2,1.9,3.2,6.8,9.3,2.4,3.7,4.0,8.9,6.2,5.9,7.5])

x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.2,random_state=42)

model=RandomForestRegressor(n_estimators=10)
model.fit(x_train,y_train)

pred=model.predict(x_test)

print("Actual values:", y_test)
print("Predicted values:", pred)
print("R2 Score:", r2_score(y_test, pred))

