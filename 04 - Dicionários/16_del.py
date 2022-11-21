import os
os.system("cls")

# Metodo del = Remove o uma atributo ou chave do dicionario 
# 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}


del contatos["guilherme@gmail.com"]["telefone"] # Exclui o telefone
print(contatos)
del contatos["chappie@gmail.com"] # Exclui a chave e seus atributos

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)


carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
w = carro.get("motor")
print(w)