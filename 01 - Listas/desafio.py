# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;

import os
os.system("cls")

letra = input() 


# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # Lista com letras do Alfabeto

contador = 0
while contador < 26:
  if (letra.upper() == letras[contador]):
    print(contador + 1)
  contador = contador + 1
  
while True:
    opt=input()
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
        if (opt.upper() == "ESQUERDA"):
          print("ingles")
        elif (opt.upper() == "DIREITA"):
          print("frances")
        elif (opt.upper() == "AMBAS"):
          print("caiu")
        elif (opt.upper() == "NENHUMA"):
          print("portugues")
        else:
          print("Informe opcção valida!!")
    except EOFError: 
        break
  