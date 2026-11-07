from sklearn.svm import SVR #SVM supports SVR and SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import numpy as np

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([1.2,1.9,2.4,3.7,4.0])

sc_x=StandardScaler()
sc_y=StandardScaler()

x_std=sc_x.fit_transform(x)
y_std=sc_y.fit_transform(y.reshape(-1,1))

model=SVR(kernel='rbf')
model.fit(x_std,y_std)

pred=model.predict(x_std)

print(r2_score(y_std,pred))

