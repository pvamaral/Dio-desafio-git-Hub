import os
os.system("cls")

#
# Listas = Definida com []
#

lista = ["casa", "banana","ceasa",10, 75,"gato"]
print(lista)

# Para saber o niumero de elementos de uma lista
print(len(lista))
# Como saber se um elemento pertence a uma lista
print("opala" in lista)
print("banana" in lista)

# remover elemento da lista 
print(lista)
lista.remove(10)
print(lista)

# Adicionar elemento a lista 
print(lista)
lista.append("Orangotango")
print(lista)

# Adicionar mais de um elemento a lista 
print(lista)
lista.extend(["rango",'Robalo'])
print(lista)



nova_lista = [0,30,55,68,78,995,300,20,55]

# Maior valor da lista

print(max(nova_lista))

# menor valor da lista

print(min(nova_lista))

# Ordenar lista

nova_lista.sort()
print(nova_lista)

# Contar quantas vezes um elemento aparece na lista
print(nova_lista.count(55))

#
## T U P L A S  =====> Os valores da tupla são imutaveis - Definidas com ()
#

tp=("casa", "banana","ceasa",10, 75,"gato")
print(tp)
print(tp.count("ceasa"))
print(tp[2:3])

#
# Dicionarios + definidos com {} - É constituido de um  conceito de chave(indice) + Valor
#
 
dicionario = {"paulo":54,"Junia":53,"Bernardo":15,"Thor":7}
print(dicionario["Junia"])

# retorna as chaves do dicionario
print(dicionario.keys())

# retorna as chaves do dicionario
print(dicionario.values())

# Verifica se existe uam chave no dicionario, se existir ele retona o valor, caso naop exista ele insere a nova chave como valor
dicionario.setdefault("jorge",33)

print(dicionario.values())

# Atualizar valor do dicionario

dicionario["Junia"]= 54
print(dicionario.values())

