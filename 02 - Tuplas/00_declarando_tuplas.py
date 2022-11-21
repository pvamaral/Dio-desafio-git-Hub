import os
os.system("cls")

# A tupla é uma lista que os elementos são imutaveis até o fim do processamento
#
# Para se definir a tupla é boa pratica colocar a virgula apos o ultimo elemento
# Por ser imutavel so permite poucos metodos - count, index, len

carros = ("gol")
print(isinstance(carros, tuple))


frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

# ('laranja', 'pera', 'uva')    
#       0        1       2
#      -3       -2      -1

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
