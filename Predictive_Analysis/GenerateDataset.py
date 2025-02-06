import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerando dados de séries temporais
np.random.seed(42)

# Definindo o número de períodos
periodos = 365 * 2  # 2 anos de dados diários

# Gerando uma série temporal de datas diárias
datas = pd.date_range(start="2022-01-01", periods=periodos, freq="D")

# Criando uma tendência (exemplo: aumento linear com tendência sazonal)
tendencia = np.linspace(0, 20, periodos)

# Gerando variação sazonal (sinusoidal para representar variações sazonais)
sazonalidade = 10 * np.sin(np.linspace(0, 3.14 * 2, periodos))

# Gerando um ruído aleatório
ruido = np.random.normal(0, 5, periodos)

# Criando o valor da série temporal (tendência + sazonalidade + ruído)
valores = tendencia + sazonalidade + ruido

# Criando o DataFrame com as datas e os valores
df = pd.DataFrame({"Data": datas, "Valor": valores})

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Visualizando a série temporal
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Valor'], label='Valor', color='blue')
plt.title('Série Temporal Fictícia')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
plt.show()
