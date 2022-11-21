import os
os.system("cls")

# É necessarioiniciar a função com def <Nome da função>

def exibir_mensagem(): # É necessarioiniciar a função com def <Nome>
    print("Olá mundo!")


def exibir_mensagem_2(nome):  # É necessarioiniciar a função com def <Nome da função>  (nome => Parametro)
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
