import os
os.system("cls")

# Podemos agrupar parametros obrigatotrios posicionais = Somente por posicção (não nominados)
# Para determinar quais os argumentos são só por posição utilizamos o caracter /
#          argumentos só por posição/
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
