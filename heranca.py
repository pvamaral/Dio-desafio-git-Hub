import os
os.system("cls")

class Veiculos:
    def __init__(self, cor, placa, numero):
        self.cor = cor
        self.placa = placa
        self.numero = numero
    
    def ligarmotor(self):
        print("Ligando Motor!!")
        
class Motos(Veiculos):
      pass

class Carros(Veiculos):
      pass

class Caminhoes(Veiculos):
    def __init__(self, cor, placa, numero, carregado):
        super().__init__(cor, placa, numero) # Chama a implementação da classe Python
        self.carregado=carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado") 
    
moto = Motos("Roxa","GWW 1518",2)

print(moto)
moto.ligarmotor()

carro = Carros("branco","XYZ 1518",4)
print(carro)
carro.ligarmotor()

caminhao = Caminhoes("Verde","PTT 1518",18, False)
print(caminhao)
caminhao.ligarmotor()
caminhao.esta_carregado()