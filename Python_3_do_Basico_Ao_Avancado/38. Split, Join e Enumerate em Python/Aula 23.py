"""
Split, Join, Enumerate em Python
* Split - dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #iteraveis
"""

string = "O Brasil é o o o país do futebol, o Brasil é penta."

lista = string.split(" ")

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)

for indice, palavras in enumerate(lista):
    print(indice,"-",palavras)
