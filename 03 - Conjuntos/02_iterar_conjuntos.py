import os
os.system("cls")

# Um set é uma coleção que possui elementos que não estão duplicados - Ele nao garante a ordem de retorno dos elementos - ele pode retornar fora de ordem 
# Set não suporta indexação
# Para se acessar os dados de forma indexado é necessário transfor o set em uma lista ou pesquisa-lo dentro de um for com o enumerate

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
