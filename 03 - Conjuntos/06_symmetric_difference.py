import os
os.system("cls")

# Um set é uma coleção que possui elementos que não estão duplicados - Ele nao garante a ordem de retorno dos elementos - ele pode retornar fora de ordem 
# Set não suporta indexação
# Para se acessar os dados de forma indexado é necessário transfor o set em uma lista ou pesquisa-lo dentro de um for
# Podemos fazer operação com o set iguas as que fazemos na matematica com conjuntos 

# Diferença simetrica - Todos os elementos que não estão na interseção

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)
