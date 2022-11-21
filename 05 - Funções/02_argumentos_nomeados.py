import os
os.system("cls")

# Argumento nomeado é o conjunto chave valor
# A vantagem de se usar o argumento nomeado é que ele garante os valores nos atributos corretos

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Argumento nomeado
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Os dois asterisco informa que é um dicionario que esta sendo passado como argumento
