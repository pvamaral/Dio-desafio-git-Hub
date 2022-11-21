import os
os.system("cls")

# O sorted é uma funçaõ que ja esta definida na linguagem  - ela constroi uma nova lista com os parametros de ordenação

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

[n**2 if n > 6 else n for n in range(10) if n % 2 == 0 print(n)]