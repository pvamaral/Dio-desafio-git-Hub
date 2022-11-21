import os
os.system("cls")

# Metodo fromkeys = Ele cria chaves  para um dicionario com conteudo vazio ou valor padrão

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
