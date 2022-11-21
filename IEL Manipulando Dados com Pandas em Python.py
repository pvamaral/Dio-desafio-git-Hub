# Para instalar biblioteca pandas ou qualquer outra
# Digite no terminal
# pip install pandas (ou o nome da outra biblioteca)
# ou python -m pip install pandas


import pandas as pd

# Storing dataset on Dataframe df1
url = "https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv"
df1=pd.read_csv(url)
df1.head()
# Storing dataset on Dataframe df1
url = "https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv"
sf = pd.read_csv(url)
sf.head()