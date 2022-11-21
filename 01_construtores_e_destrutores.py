


class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado
        
    def fala(self):
        print("auaua")
        
    def __del__(self):
        print("Removendo a instancai da classe")
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)
        
        
criar_cachorro()