import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 3.5, 4.1, 5])

# Reshape os dados de entrada (necessário quando você tem apenas uma feature)
x = x.reshape(-1, 1)

# Crie um modelo de regressão linear
model = LinearRegression()

# Ajuste o modelo aos dados
model.fit(x, y)

# Faça previsões com o modelo
y_pred = model.predict(x)

# Plote os dados reais e as previsões
plt.scatter(x, y, label='Dados Reais')
plt.plot(x, y_pred, color='red', label='Regressão Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Imprima os coeficientes da reta de regressão
print("Coeficiente de inclinação (slope):", model.coef_[0])
print("Coeficiente de interceptação:", model.intercept_)
