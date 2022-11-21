import os
os.system("cls")

# Metodo keys = Retorna só as chaves de um dicionario - 
# 

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)
