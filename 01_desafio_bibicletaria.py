import os
os.system("cls")


# POO- Orientado ao Objeto
# 

# Criando a classe = criando a partir de um metodo construtor

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):   # I M P O R T A N T E :      __init__  (dois underlines)
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = 18
    
    def buzinar(self):
        print("Plim Plim !!!")

    def parar(self):
        print("Parando a Bicicleta !!")
        print("Parou !!!")

    def correr(self):
        print("Vrummm  !!!")
        
    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"      
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([ f' {chave}={valor}' for chave, valor in self.__dict__.items()])}"       
        
        
b1 = Bicicleta("vermelha", "Caloi", 2022, 600, 29)
    
#caloi = Bicicleta("vermelha", "caloi",2022, 600)

b1.buzinar()
b1.correr()
b1.parar()


b2 = Bicicleta("vinho", "Monark", 2022, 600, 26)
print(b2)


