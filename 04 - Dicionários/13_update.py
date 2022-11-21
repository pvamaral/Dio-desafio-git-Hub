import os
os.system("cls")

# Metodo values = ele retorna só os valores daquele dicionario - Nãp retona as chaves
# 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})   
## Se voce pedir o update de duas cheves parametros por uma só ele vai susbstituir 
# {"nome": "Guilherme", "telefone": "3333-2221"} por somente # {'guilherme@gmail.com': {'nome': 'Gui'}}
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# Se a chave não existir ele criará ===> {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
