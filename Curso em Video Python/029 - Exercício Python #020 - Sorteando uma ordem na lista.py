'''

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''
# Bibliotecas iniciais
from random import choice, shuffle

# Lista vazia para iniciar
lista = []

# pedido dos nomes dos alunos

arquivotxt =  open('Nomes dos alunos.txt','r',encoding='UTF-8')
listadoslunos = arquivotxt.readlines()

for indice, nomes in enumerate(listadoslunos):
    print(f'{nomes}')