import os
os.system("cls")

# Um set é uma coleção que possui elementos que não estão duplicados - Ele nao garante a ordem de retorno dos elementos - ele pode retornar fora de ordem 
# Set não suporta indexação
# Para se acessar os dados de forma indexado é necessário transfor o set em uma lista ou pesquisa-lo dentro de um for
# Podemos fazer operação com o set iguas as que fazemos na matematica com conjuntos 

# add (Se o elemento não existir ele adiciona no conjunto)

sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
