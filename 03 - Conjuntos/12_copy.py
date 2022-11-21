import os
os.system("cls")

# Um set é uma coleção que possui elementos que não estão duplicados - Ele nao garante a ordem de retorno dos elementos - ele pode retornar fora de ordem 
# Set não suporta indexação
# Para se acessar os dados de forma indexado é necessário transfor o set em uma lista ou pesquisa-lo dentro de um for
# Podemos fazer operação com o set iguas as que fazemos na matematica com conjuntos 

# copy (copia o conjunto)

sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}
