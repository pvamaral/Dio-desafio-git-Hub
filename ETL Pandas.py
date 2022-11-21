import os
os.system("cls")
#
# Import pandas package 
#

from glob import escape
from statistics import linear_regression
import pandas as pd 
    
import os
os.system("cls")

df.shape # Exibe a quantidade de linhas e colunas da base de dados
df.head(4)  # Exibe a s quatro primeiras linhas do Dataframe
df.info() # Qual o formato de (tipo) dados de cada coluna e a memoria utilizada pelo conjunto de dados
df.columns 
df.isnull().sum() ## verificar dados faltantes no conjunto de dados
df['setor'].unique()  # Verifica os valores unicos em determinada coluna
df["setor"].value_counts.plot(kind='bar') # Gera grafico a partir de grupamentos
df.describe() # Informa dados estatisticos sobre a base de dados


#
# Scikit Learn ( uma das principais de machine learning e inteligencia artificial)
#

from sklearn.linear_model import LinearRegression

#Problema  = 200 observações
#             1   variavel preditora e noise de 30 (intervalo)

# Gerando massa de dados

x,y = make_regression(n_samples = 200, n_features = 1, noise = 30)

# Para plotar os parametros gerados acima

import matplotlib.pyplot as plt

# Mostrando o grafico
plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color='red', linewidth=3 )
plt.show()

# Criação do modelo

modelo = Linear_Regression()


