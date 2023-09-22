import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 50)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 10, 50)
# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

mse = mean_squared_error(y,y_pred)
r2 = r2_score(y,y_pred)
print("Mean squared error: %.2f" % mse)
print("Coefficient of determination: %.2f" % r2)

plt.scatter(x, y, s=10)
plt.plot(x, y_pred, color='r')
plt.show()