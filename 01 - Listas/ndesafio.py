salario = int(input()) 
nsalario = 0
reajuste = 0
percentual = 0

if (salario <= 600):
   percentual = 1.17
elif (salario > 600 and salario <= 900):
   percentual = 1.13
elif (salario > 900 and salario <= 1500):
   percentual = 1.12
elif (salario > 1500 and salario <= 2000):
   percentual = 1.10
else: 
   percentual = 1.05

nsalario = salario * percentual
reajuste = nsalario - salario
print(f"Novo salario {nsalario:.2f} ")
print(f"Reajuste ganho: {reajuste:.2f}\n")
print(f"Em percentual: {(percentual * 100) - 100:.2f} %")