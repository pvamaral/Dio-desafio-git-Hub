import os
os.system("cls")

# Dicinario aninhado é uma dicionario de dados dentro de outroa dicionario - Um objeto dentro de um objeto


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)
w_string = contatos["pvamaral@uol.com.br"]["telefone"]
print(w_string)
w_string = contatos["pvamaral@uol.com.br"]["extra"]
print(w_string)

print(contatos)
