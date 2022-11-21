import os
os.system("cls")

# É necessarioiniciar a função com def <Nome da função>
# O resultado da função é passado pelo return

def calcular_total(numeros):
    return sum(numeros)

def calcular_total_m(N1, N2, N3):
    c = N1 + N2 + N3
    return c

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print (calcular_total_m(1,2,3))
print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
