frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

numeros = [1, 10, 20, 35, 66, 33, 49, 74. ,1800, 65, 28]
pares = []
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
print(quadrado)


