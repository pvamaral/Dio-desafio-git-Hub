import os
os.system("cls")

# Dicinario aninhado é uma dicionario de dados dentro de outroa dicionario - Um objeto dentro de um objeto



contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])  # Para exibir o conteudo de cada chave é necessário acrescentar o contatos["chave"]

print("=" * 100) # Imprime 100 caracteres de "="

for chave, valor in contatos.items():
    print(chave, valor)
