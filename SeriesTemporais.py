import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregando o conjunto de dados 'Diabetes'
diabetes = load_diabetes()

# Utilizando a variável 'data' que contém as medições dos dados dos pacientes
data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# Vamos escolher uma das variáveis, como 'bmi' (Índice de Massa Corporal) como exemplo de série temporal
bmi_series = data['bmi']

# Criando um índice temporal (neste caso, uma série de números representando uma linha do tempo)
# Para simplificação, vamos criar um índice de datas a partir de uma data inicial
time_index = pd.date_range(start='1/1/2000', periods=len(bmi_series), freq='D')

# Criando uma série temporal
bmi_series.index = time_index

# Plotando a série temporal
plt.figure(figsize=(10, 6))
plt.plot(bmi_series, label='Índice de Massa Corporal (BMI)', color='b')
plt.title('Índice de Massa Corporal (BMI) ao longo do tempo')
plt.xlabel('Ano')
plt.ylabel('Índice de Massa Corporal (BMI)')
plt.legend()
plt.show()

# Decompondo a série temporal para ver tendência, sazonalidade e erro
decomposition = seasonal_decompose(bmi_series, model='additive', period=365)

# Plotando a decomposição
plt.figure(figsize=(10, 8))

plt.subplot(411)
plt.plot(bmi_series, label='Original', color='b')
plt.legend(loc='best')
plt.title('Série Temporal Original')

plt.subplot(412)
plt.plot(decomposition.trend, label='Tendência', color='r')
plt.legend(loc='best')
plt.title('Tendência')

plt.subplot(413)
plt.plot(decomposition.seasonal, label='Sazonalidade', color='g')
plt.legend(loc='best')
plt.title('Sazonalidade')

plt.subplot(414)
plt.plot(decomposition.resid, label='Resíduo', color='orange')
plt.legend(loc='best')
plt.title('Erro')

plt.tight_layout()
plt.show()

# Exemplo de previsão simples (média móvel)
bmi_series_rolling_mean = bmi_series.rolling(window=30).mean()

# Plotando a série temporal com a média móvel
plt.figure(figsize=(10, 6))
plt.plot(bmi_series, label='Índice de Massa Corporal (BMI)', color='b')
plt.plot(bmi_series_rolling_mean, label='Média Móvel (30 dias)', color='r', linewidth=2)
plt.title('Índice de Massa Corporal com Média Móvel')
plt.xlabel('Ano')
plt.ylabel('Índice de Massa Corporal (BMI)')
plt.legend()
plt.show()