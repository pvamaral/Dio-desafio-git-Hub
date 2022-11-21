import os

os.system("cls")

# Manipulação de stringd

V_texto = (input("Informe o texto a ser manipulado: "))

# Transforma string em maiuscula
print(V_texto.upper())
# Transforma string em minuscula
print(V_texto.lower())
# Transforma string em titulo
print(V_texto.title())
# Remove espaços da string
print(V_texto.strip())
# Remove espaços à direita da string
print(V_texto.rstrip())
# Remove espaços à esquerda da string
print(V_texto.lstrip())
# Remove espaços à esquerda da string
print(V_texto.lstrip())
# Centraliza o texto da strinbg e complementa com o caracter desejado
print(V_texto.center(50,"@"))
# Junta o caracter com a string
print("-".join(V_texto))
# Interpolação de variaveis

V_nome = "Paulo Vito"
V_idade = 54
V_profissao = "MEI"
V_linguagem = "Python"

# Argumanetos de interpolação
# 1o metodo - utilizar - % (Não é aconselhavel o uso)
# %s - string
# %d - Inteiros
# %f - ponto flutuante (real)

print(" 1)Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. " % (V_nome, V_idade, V_profissao, V_linguagem))
# 2o metodo - utilizar - {} - format
print(" 2)Ola, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. ".format(V_nome, V_idade, V_profissao, V_linguagem))
# 3o metodo - utilizar - {N} - format : Onde N é o numero da sequencia do campo
print(" 3)Ola, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}. ".format(V_nome, V_idade, V_profissao, V_linguagem))
# 4o metodo - utilizar - {campo} - format : Onde campo é o nome da variavel de referencia do campo
print(" 4)Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profisao} e estou matriculado no curso de {linguagem}. ".format(nome=V_nome, idade = V_idade, profisao = V_profissao, linguagem = V_linguagem))
# 5o metodo - utilizar o dicionaria para definir um obejto (Pessoa)
Pessoa = {"nome":"Paulo Vito O.", "idade": 54, "profissao" : "tatuador", "curso": "Strip-tease"}
print(" 5)Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {curso}. ".format(**Pessoa))
# 6o metodo - fstring utilizar - f e {Variavel}
print(f" 6)Ola, me chamo {V_nome}. Eu tenho {V_idade} anos de idade, trabalho como {V_profissao} e estou matriculado no curso de {V_linguagem}. ")

# Formatação com f_string - Define o numero de casas decimais {PI:.2f}
#                                                             {PI:10.2f}
PI = 3.1419
print(f"O valor de PI é  : {PI:.2f}")
print(f"O valor de PI é  : {PI:10.2f}")

# Fatiamento de string (Substr)

V_pnome = V_nome[0:5] # Da posicao 0 + 5 posições
print (f" substr de 01 a 5 {V_pnome}")
V_pnome = V_nome[2: 3] # Da posição 2 + 1 posição
print (f" substr de 02 a 3 {V_pnome}")
V_pnome = V_nome[:5] # Da posição 0 + 5 posição
print (f" substr de 0 a 5 {V_pnome}")
V_pnome = V_nome[8:] # Da posição 8 ate o fina da string  
print (f" substr de 8 a max {V_pnome}")
V_pnome = V_nome[::-1] # Inverte a ordem das string
print(f" :: -1 {V_pnome}")
# Strings de multiplas linhas 
# Definidas por """ o inicio e no final da variavel

V_mensagem = f"""
   Ola , meu nome é {V_nome},
eu estou aprendendo {V_linguagem}
   Esta mensagem te diferentes recuos"""

print(V_mensagem)