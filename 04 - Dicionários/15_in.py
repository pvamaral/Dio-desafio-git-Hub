import os
os.system("cls")

# Metodo in = Metodo elegante de e saber se uma chave existe ou não no dicionario
# 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "pvamaral@uol.com.br": {"nome": "Paulo Vito", "telefone": "999564519","extra": {"a":1}},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False = Verifica se existe idade associada a esta chave
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

# A utilização do in poderia ser substituida pelo script abaixo

#lista_chaves: list = contatos.keys()  # Pega todas as chaves do dicionario
#ct = lista_chaves.index("pvamaral@uol.comm.br")
#print(f" Index {ct}")
#ct = lista_chaves.count("pvamaral@uol.comm.br")

