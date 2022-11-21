import os
os.system("cls")

# Metodo get = 2a forma de voce acessar valores de um dicionario - 
# 
# I M P O R T A N T E
# 
#Se voce não tem certeza de que a chave existe no dicionario utilie o get

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

contatos = {"idioma": "pt_br", "pais": "Brasil" }
print(contatos["pais"])