
# Importando as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn") 

# Fazerndo upload das tabelas

# Upload do Arquivo
from google.colab import files
arq = files.upload()

# Criando Data Frame

df=pd.read_excel("AdventureWorks.xlsx")

df.head()

df.shape

df.dtypes

# Qual o total de venda
df["Valor Venda"].sum()

# Qual o custo total - Calcula e cria a coluna custo
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])

df.head(5)

# Qual o custo total 
round(df["custo"].sum(),2)

# Qual o lucro 
df["lucro"] = df["Valor Venda"] - df["custo"]
df.head(5)

# Qual o lucro total 
round(df["lucro"].sum(),2)

# Cria coluna com o numero total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# Verificando se temod dados faltantes
df.isnull().sum() 

# Qual o lucro por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

# mudar a mascara de apresentação do numero
pd.options.display.float_format = '${:,.2f}'.format

# Resetando o indice
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()

# Qual o total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False)

# Criando o grafico - basta adicionar o .plot com os respectivos parametros no final do groupby
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False).plot.barh(title="Produtos Vendidos")

# Cria grafico de barras - Lucro X Receita
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title = "Lucro X ano")
plt.xlabel="Ano"
plt.ylabel="Receita"

# Criando Data frame somente com os dados de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

# Criando grafico 
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title=" Lucro Mes - 2009")

# Lucro por marca
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title=" Lucro Mes - 2009")
plt.xlabel=("Marca")
plt.ylabel=("Lucro")
plt.xticks(rotation="horizontal");  ## O titulo da barra fica na horizontal

# Lucro por classe
df_2009.groupby("Classe")["lucro"].sum().plot.bar(title=" Lucro X Classe - 2009")
plt.xlabel=("Classe")
plt.ylabel=("Lucro")
plt.xticks(rotation="horizontal");



# Grafico de Boxplot 
plt.boxplot(df["Tempo_envio"]);

# Grafico de Histograna
plt.hist(df["Tempo_envio"]);

## Outlier = Valor discrepante
# Como localizar o Outlier
df[df["Tempo_envio"]== 20]

# Para salvar um novo arquivo
df.to_csv("df_vendas_novo_csv", index = False)