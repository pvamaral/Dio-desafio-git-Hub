import os
os.system("cls")

# Metodo setdefault = determina o valor defult para um atributo - Se o atributo não existir ele cria, caso contrario ele respeita o valor do dicionario
# 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}
contatos.setdefault("nome", "Giovanna")  # "Guilherme"     =======> O atributo nome já exite e ele respeita
print(contatos)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contatos.setdefault("idade", 28)  # 28  =======> O atributo idade não existe ele cria com o valor default 
print(contatos)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
