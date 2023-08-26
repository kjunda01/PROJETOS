'''

Desafio 09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

'''

while True:
    try:
        numero = int(input('Digite o número para a tabuada: '))
        print(f'Tabuada do número: ({numero})')
        for tabuada in range(1,11):
            print(f'({tabuada}) x ({numero}) = ({tabuada * numero})')
            continue
    except ValueError:
        print('Digite apenas números inteiros.\n')