import os

os.system("cls")

V_inteiro = 1
V_String = "Banana"
print(V_inteiro)
print(float(V_inteiro))
print(str(V_inteiro))
print(type(V_inteiro))
print(type(V_String))
print(10/3)
print(10//3)
V_nome = input("Informe seu Nome: ")
V_Sobrenome = input("Informe seu Sobrenome: ")
V_idade = input(" Informe sua Idade : ")
print(f"Nome: {V_nome} e Sobrenome {V_Sobrenome}" , end = "...\n")
print(f"Nome: {V_nome} e Sobrenome {V_Sobrenome}")
print(V_nome , V_Sobrenome)
print(V_nome , V_Sobrenome, end ="...\n")  # Coloca o final da linha como ...
print(V_nome , V_Sobrenome, sep ="#")      # Substitui o separador por #