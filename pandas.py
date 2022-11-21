# Para instalar biblioteca pandas ou qualquer outra
# pip install pandas (ou o nome da outra biblioteca)
# ou python -m pip install pandas

import pandas as pd
import os
os.system("cls")

# Importando biblioteca pandas

# Cria um dataframe df a partir da leitura do arquivo csv 
#   O parametro error_bad_lines=False   - Despreza as linhas com problemas
#   O Parametro sep = ";"  define o separador de campos, o default normalmente é ",", mas neste arquivo o separador é ";"

df = pd.read_csv("D:\Meu Drive\Colab Notebooks\datasets\Gapminder.csv",error_bad_lines=False,sep=";")

# Mostra as 5 primeiras linhas do dataframe df

df.head()
df.head(10)  # Mostra as 10 primeiras linhas

# Mostra as 5 ultimas linhas do dataframe df

df.tail()
df.tail(10)  # Mostra as 10 ultimas linhas

# Muda os nomes das colunas

df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de Vida", "gdpPercap":"PIB"})


# Retorna o total de linhas e a quantidade de colunas
df.shape

# Retorna o nome das colunas
df.columns

# Retorna o tipo dos dados das colunas
df.dtypes


# Retorna informações estatistica da base de dados (Quartis, valor minimo, valor maximo, media, maximo)
df.describe()

# Retorna os valores unicos da coluna continente

df["Continente"].unique()

# Fazer filtro no data type ======> É criada a variavel oceania e pedimos para localizar no data frame todas as linhas que atendem aquela condição
oceania = df.loc[df["continent"] == "Oceania"]
# Para confirmar usar o mesmo comando para retornar os valores unicos, só que na nova variavel oceania
oceania["continent"].unique()

# Para agrupar paises por continente 

df.groupby("continent")["country"].nunique() # Retorna o nunmero de paises por continente
df.groupby("continent")["country"].unique() # Retorna os  paises por continente

# Calcula a expectativa meia de vida por ano
df.groupby("year")["lifeExp"].mean()

# Calcula a media de uma coluna
df["gdpPercap"].mean()

# Calcula a soma de uma coluna
df["gdpPercap"].sum()

# 
#    Para ler planilhas Excell com Pandas
#

# Importando a biblioteca
import pandas as pd

# Leitura das planilhas Excell - Definindo um data frame para cada planilha
df1= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/datasets/Aracaju.xlsx")
df2= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/datasets/Fortaleza.xlsx")
df3= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/datasets/Natal.xlsx")
df4= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/datasets/Recife.xlsx")
df5= pd.read_excel("/content/drive/MyDrive/Colab Notebooks/datasets/Salvador.xlsx")

# Concatenando todos os data frames em uma unica planilha

df = pd.concat([df1, df2, df3, df4, df5])

# Exibe as 5 primeiras linhas
df.head()

# Mostra as 5 ultimas linhas do dataframe df
df.tail()

# Pedir uma amostr de N linhas do Data Frame = df.sample(N)
df.sample(10)

# Retorna o tipo dos dados das colunas
df.dtypes

# Alterar  tipo de dado de uma determinada coluna 
df["LojaID"] = df["LojaID"].astype("object")

# Verificar linhas do Data frame com valores faltantes (null)
df.isnull().sum()

# Substituindo os valores nulos pelo valor da media 

#
# O parametro fillna seleciona automaticamente os valores nulos - todo os paramentros que terminarem em na se referem a null
#

df["Vendas"].fillna(df["Vendas"].mean(),inplace = True)

# Substituindo os valores nulos pelo numero 0 (ZERO)
df["Vendas"].fillna(0,inplace = True)

# Apagar linhas com valores nulos
df.dropna(inplace=True)

# Apagar as linhas com valores nulos com base em apenas uma coluna
df.dropna(subset = ["Vendas"], inplace=True)

# Apagar as linhas com valores nulos com base em todas as colunas
df.dropna(how = "all", inplace=True)

# Criar novas colunas  - Criar coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Pegar o valor minimo de uma coluna
df["Receita"].min()

# Pegar o valor maximo de uma coluna
df["Receita"].max()

# Pega o top N com base na coluna receita do Data Frame   df.nlargest(N, "Receita")
df.nlargest(3, "Receita")

# Pega as N piores com base na coluna receita do Data Frame   df.nsmallest(N, "Receita")
df.smallest(3, "Receita")

# Agrupando por cidade - Total de receita
df.groupby("Cidade")["Receita"].sum()

# Ordenar o conjunto de dados pela coluna receita  e exibe as 10 primeiras linhas
df.sort_values("Receita", ascending=False).head(10)


#
#
#
#   Trabalhando com Datas
#
#
#

# Para transformar a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

df.dtypes

# Para transformar a coluna de data (int64) em tipo data
df["Data"] = pd.to_datetime(df["Data"])

# Agrupando valores por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

df.sample(10)

# Extraindo o mes e o dia da data - criando novas colunas
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day,)

# Retornando a data mais antiga
df["data"].min()

# Calculo de diferenca de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

# filtrando asa vendas de 2019 do Mes de Março == Craindo a variavel vendas_marco_19
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Exibe 20 linhas de exemplo da variavel
vendas_marco_19.sample(20)

# Conta a quantidade de registro por loja
df["LojaID"].value_counts(ascending=False)

#
#
#
#   G R A F I C O S
#
#
#
#

# Faz um grafico de barra VERTICAL por quantidade de registros por loja
df["LojaID"].value_counts(ascending=False).plot.bar()

# Faz um grafico de barra HORIZONTAL por quantidade de registros por loja
df["LojaID"].value_counts(ascending=False).plot.barh()

#### Se n~çao quiser exibir o descritivo do grafico no tpo, bast acarescrenatr ; ao final do comando
df["LojaID"].value_counts(ascending=False).plot.barh();

# Grafico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# Total de vendas por cidade 
df["Cidade"].value_counts()

# criar grafico de pizza Total de vendas por cidade 
df["Cidade"].value_counts().plot.pie()

# Cria grafico de linha Total de vendas por cidade 
df["Cidade"].value_counts().plot()

# Adicionando um titulo e alterando o nome dos eixos = Inclui titulo
# A cor default do grafico é azul, se quiser alterar a cor, basta acrescentar paramanetro color  e definir a cor desejada

#
import matplotlib as plt
# 


df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade")
df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color = "green")
plt.xlabel("Total de Vendas")
plt.ylabel("Total de Vendas")

# O estilos dos graficos do matplot podem ser alterados conforme : https://matplotlib.org/stable/gallery/index.html

# Alterando o estilo do grafico
plt.style.use("ggplot")
# Adicionando um titulo e alterando o nome dos eixos

#
import matplotlib.pyplot as plt
#


df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color = "green")

# criando nova variavel somente com os dados de vendas de 2019 - O paramaetro marker define o marcado do grafico ====> Grafide linha
df_2019 = df[df["Ano_Venda"] == 2019]

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.legend

# Plotando um histograma
plt.hist(f["Qtde"], color = "magenta");


# Plotando Grafico de dispersão
plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"],color = "red");

#
# Gerar e salvar grafico = Ofico sera gravado como png na aba files e poderá ser baixado
#

df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color = "green")
plt.xlabel("Cidades")
plt.ylabel("Total de Vendas")
plt.savefig("grafico teste")