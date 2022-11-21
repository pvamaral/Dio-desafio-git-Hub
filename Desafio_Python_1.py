# Author: Paulo Vito 
# Desafios Iniciais Py - Unimed-BH
# 1 / 3 - As Duas Torres

import os
os.system("cls")
V_y = 0              # Diamentro Saruman
V_x = 0              # Diametro Sauron
V_n = 0              # Distancia
V_Icm = 0.0

V_n = int(input(" Informe o valor da Distancia (N): "))
if (V_n > 0) and (V_n < 10000):
    V_x = int(input(" Informe o diametro do Palantir de Sauron (X) : "))
    if (V_x > 0) and (V_x < 100):
        V_y = int(input(" Informe o diametro do Palantir de Saruman (Y): "))
        if (V_y > 0) and (V_y < 100):
            V_icm = V_n / ( V_x + V_y)
            print(f" O valor do ICM é  : {V_icm:.2f}")

        else:
            print("Valor do Parantir de Saruman (Y) é invalido !!!")
    else:
        print("Valor do diametro do Palantir de Sauron (X) é invalido !!!")
else:
    print("Valor da Distancia (N) é invalido !!!")

