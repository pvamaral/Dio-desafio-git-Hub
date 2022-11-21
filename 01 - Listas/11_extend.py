import os
os.system("cls")

# O extend aumenta uma lista em lote - o Append aiciona de 1 em um elemento - no extend eu posso adicionar uma nova lista

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
