import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Gerar dados de exemplo com multicolinearidade
X, y = make_regression(n_samples=100, n_features=2, noise=0.5, random_state=42)

# Adicione multicolinearidade aos dados
X[:, 1] = 2 * X[:, 0] + np.random.normal(0, 0.5, size=len(X))

# Crie um modelo de regressão linear
model = LinearRegression()

# Ajuste o modelo aos dados
model.fit(X, y)

# Imprima os coeficientes da reta de regressão
print("Coeficientes da regressão:")
print(f"Coeficiente de inclinação (slope): {model.coef_[0]}")
print(f"Coeficiente de inclinação com multicolinearidade (slope): {model.coef_[1]}")
print(f"Coeficiente de interceptação: {model.intercept_}")
