'''

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''
# Bibliotecas iniciais
from random import choice

# Lista vazia para iniciar
lista = []

# pedido dos nomes dos alunos
while '' not in lista:
    aluno = input('Digite o nome do aluno para sorteio: ')
    print('Aperte a tecla ENTER, sem digitar nada, para começar.')
    lista.append(aluno)

# Iniciando o sorteio
print('Muito bem, iniciando o sorteio....')


print('Alunos na lista de sorteio:')
for indice, nomes in enumerate(lista[:-1]):
    print(f'Aluno: ({indice+1}) = {nomes}')
print(f'\nQuantidade de alunos na lista de sorteio: [{len(lista)-1}]')

print('Sorteando....')

sorteio = choice(lista)

print(f'O aluno sorteado foi: {choice(lista)}')
