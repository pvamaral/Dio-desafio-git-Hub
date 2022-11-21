import os

os.system("cls")

# Adição
print( 1+ 3)
# Subtração
print( 10 - 3)
# Divisão
print( 10 / 3)
# Módulo - Resto da Divisão
print( 10 % 3)
# Divisão - Só a parte Inteira
print( 10 // 3)
# Multiplicação
print( 10 * 3)
# Exponenciação
print( 3 ** 3)
## Ordem de execução dos calculos 
# Executa primeiro o que esta dentro dos ()
# Executa em segundo  os Expoentes
# Executa em terceiro Multipilcação e divisão da esquerda para a direita
# Executa em terceiro Adição e Subtração da esquerda para a direita
print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 ** 2))
print(10 / 2 * 4)

# Operadores de comparação
# Igualdade ==
# Não igualdade != 
# Maior >  e Maior igual >=
# Menor <  e Menor igual <=

V_Saldo = 450
V_Saque = 200
print(V_Saldo != V_Saque)
print(V_Saldo == V_Saque)
print(V_Saldo >= V_Saque)