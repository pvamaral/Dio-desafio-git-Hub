import os
os.system("cls")

# O Sort é um metodo que ordena os elemntos de uma lista 

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)


# O parametro reverse=True no sort   Ele ordena e tambem cria um espelhamento da lista

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# O parametro Key = lambda x:len(x) ele vai ordenar p sort pela tamanho dos elementos (lenght)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# O parametro Key = lambda x:len(x) ele vai ordenar p sort pela tamanho dos elementos (lenght)  = O parametro Reverse determina que o sorte é decrescente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
