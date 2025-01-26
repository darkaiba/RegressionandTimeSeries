import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, r2_score

# Carregando o conjunto de dados
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Criando um DataFrame para melhor visualização
df = pd.DataFrame(X, columns=diabetes.feature_names)
df['target'] = y

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Erro quadrático médio:', mse)
print('Coeficiente de determinação (R²):', r2)

# Visualizando os resultados
plt.scatter(y_test, y_pred)
plt.xlabel('Nível de Glicose Real')
plt.ylabel('Nível de Glicose Previsto')
plt.title('Predição do Nível de Glicose em Pacientes Diabéticos')
plt.show()