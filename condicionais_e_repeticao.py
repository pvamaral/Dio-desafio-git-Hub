import os

os.system("cls")

# Estruturas condicionais

V_saldo = 5000
V_Saque = float(input("Quaql o valor do Saque:"))
if V_Saque > V_saldo:
    print("Saldo Insuficinte !!")
elif V_Saque <= V_saldo:
     print(f"Saldo atual :=  {V_saldo - V_Saque}")
     print("Saque efetuado")
     V_saldo = V_saldo - V_Saque
     if V_saldo > 0:
        print("Saldo ainda positivo!!")
     else:
        print("Saldo Zerado!!")

V_status= "Saque de certo " if V_saldo >= V_Saque  else "Fudeu!!"
print(V_status)

# Estrutura de repetição
# For

V_texto = input("Informe um texto:")
V_vogais = "AEIOU"
V_Consoante = "BCDFGHJKLMNPQRSTVXYZ"
V_Cvogais = 0
V_Cconsoante = 0
for V_contador in V_texto:
    if V_contador.upper() in V_vogais:
        V_Cvogais = V_Cvogais + 1
    elif V_contador.upper() in V_Consoante:
        V_Cconsoante = V_Cconsoante + 1
print(f"Total de vogais no texto {V_Cvogais}")
print(f"Total de consoantes no texto {V_Cconsoante}")

for numero in range(0, 500, 3 ):
    print(numero, end=" ")
    if numero % 2 == 0:
       continue
    if numero == 303:
        break
print(" \n")
# While

V_opcao = 1

while V_opcao != 0: 
    V_opcao=int(input(" 1 - Continua\n 2 - Continua\n 0 - Cansei\n: "))
    

