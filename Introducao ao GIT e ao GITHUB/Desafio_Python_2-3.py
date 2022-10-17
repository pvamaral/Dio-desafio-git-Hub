# Author: Paulo Vito 
# Desafios Iniciais Py - Unimed-BH
# 2 / 3 - Cachorros Quentes

import os
os.system("cls")

V_h = 0              # Pessoas
V_p = 0              # N Hot Dogs
V_media = 0.0

V_h = int(input(" Informe o numero de participantes (h): "))
if (V_h > 0):
    V_p = int(input(" Informe o numero de Hot Dogs (p) : "))
    if (V_p > 0) and (V_p <= 1000):
        V_media = V_h / V_p
        print(f" A Media de Hot Dogs por participante é  : {V_media:.2f}")
    else:
        print("Numero de Hot Dogs é invalido !!!")
else:
    print("Numero de participantes é invalido !!!")
