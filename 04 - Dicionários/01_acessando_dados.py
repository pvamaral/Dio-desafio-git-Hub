import os
os.system("cls")

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Exibe dados

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

# Altera valor dos dados
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
