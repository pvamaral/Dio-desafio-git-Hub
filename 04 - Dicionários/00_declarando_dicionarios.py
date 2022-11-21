import os
os.system("cls")

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"} =======> Adiciona nova chave Telefone do dicionario pessoa (Objeto)
print(pessoa)
