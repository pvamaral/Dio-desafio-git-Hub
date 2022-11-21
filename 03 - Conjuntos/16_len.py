import os
os.system("cls")

# Um set é uma coleção que possui elementos que não estão duplicados - Ele nao garante a ordem de retorno dos elementos - ele pode retornar fora de ordem 
# Set não suporta indexação
# Para se acessar os dados de forma indexado é necessário transfor o set em uma lista ou pesquisa-lo dentro de um for
# Podemos fazer operação com o set iguas as que fazemos na matematica com conjuntos 

# len - informa o total de elementos do set (Não considera os redundantes)
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10
