from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Preparando os dados
df.set_index('Data', inplace=True)

# Dividindo os dados em treino e teste (70% treino, 30% teste)
train_data, test_data = train_test_split(df['Valor'], test_size=0.3, shuffle=False)

# Ajustando o modelo ARIMA (p=5, d=1, q=0 são valores comuns a se testar)
model = ARIMA(train_data, order=(5, 1, 0))
model_fit = model.fit()

# Fazendo previsões no conjunto de teste
predictions = model_fit.forecast(steps=len(test_data))

# Avaliando o modelo
mse = mean_squared_error(test_data, predictions)
print(f'Mean Squared Error (MSE): {mse}')

# Visualizando as previsões
plt.figure(figsize=(10, 6))
plt.plot(train_data.index, train_data, label='Treinamento', color='blue')
plt.plot(test_data.index, test_data, label='Teste Real', color='green')
plt.plot(test_data.index, predictions, label='Previsões', color='red')
plt.title('Previsão de Série Temporal com ARIMA')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()