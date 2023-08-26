'''

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

'''
while True:
    try:
        numero = float(input('Digite um número: '))
        parte_inteira = str(numero).split('.')[0]
        parte_decimal = str(numero).split('.')[1]
        break
    except ValueError:
        print('Digite apenas numeros reais. Ex. (1,2), (-36.45), (12)...')

print(f'O número {numero} possui a parte inteira {parte_inteira} e a parte decimal 0.{parte_decimal}')
