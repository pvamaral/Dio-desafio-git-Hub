import os
os.system("cls")

# o Escopo das variaveis pode ser local ou global - para se definir a palavra reservada global 
salario = 2000


def salario_bonus(bonus):
    global salario  # Passa a variavel salario para global 
    salario += bonus
    return salario


print(salario_bonus(500))  # 2500

def funcao(*args, **kw):,


prin(funcao("python", 2022, curso="dio")