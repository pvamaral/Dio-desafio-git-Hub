import os

os.system("cls")

# Operadores de Identidade

V_Saldo = 1000
V_Limite = V_Saldo
V_Nsaldo = 1000
print(V_Saldo is V_Limite)
print(V_Saldo is V_Nsaldo)

# Operadores de Associação

V_Curso = "Curso de Python"
V_Frutas = ["laranja","Uva","Mamão","Limão"]
print("laranja" in V_Frutas)
print("Laranja" in V_Frutas)
print("Banana" not in V_Frutas)