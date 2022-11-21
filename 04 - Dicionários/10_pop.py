import os
os.system("cls")

# Metodo pop = Ele vai remover um valor do seu dicionario = Voce passa a chave e ele remove
# 


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)
# Se o valor informado não existir no dicionario vai ser gerado um erro de key error 
# I M P O R T A N T E 
#
# Passando uma mensagem como 2o parametro voce controle este erro
resultado = contatos.pop("guilherme@gmail.com","Não encontrou")  
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
