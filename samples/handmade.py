import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import scipy as sp 


#Gera os valores a serem analisados
np.random.seed(123)
n = 100
x1 = np.random.normal(size=n)

y = 1 + 2*x1 + np.random.normal(size=n, scale=0.1)

plt.plot(x1, y, 'o')
plt.grid(color='b', linestyle='-', linewidth=1)

data = pd.DataFrame({'x1':x1, 'y':y})
data.info


#Aplica a regressão linear nos dados plotados
x_train, x_test, y_train, y_test = train_test_split(x1, y, test_size=0.20, random_state=42)
regr = linear_model.LinearRegression()

x_train = x_train.reshape(-1, 1)
x_test  = x_test.reshape(-1, 1)
regr.fit(x_train, y_train)

#predição de Ŷ utilizando o vetor de entrada de treino
y_pred = regr.predict(x_train)

#erro médio quadrático
print("Mean squared error: %2.f" % mean_squared_error(y_train, y_pred))

#coeficiente de determinação
print("Coefficient of determination: %2f" % r2_score(y_train, y_pred))

print("Coefficients: ", regr.coef_)
print("Intercept:", regr.intercept_)

plt.scatter(x_train, y_train, color="black")
plt.plot(x_train, y_pred, color="blue", linewidth=3)

plt.show()