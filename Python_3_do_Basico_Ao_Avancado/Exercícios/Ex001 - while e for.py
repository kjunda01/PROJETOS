# Exercícios estrutura de repetição

'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
'''

contador = 1
while True:
    try:
        nota = float(input('Digite uma nota: '))
        print(
            f'Você já passou aqui {contador} vezes. - Nota errada, sem erro de digitar')
        contador += 1
        if nota >= 0.0 and nota <= 10.0:
            print('Nota válida, saindo...')
            break
    except ValueError:
        print('Digite apenas uma nota entre 0.0 e 10.0')
        print(
            f'Você já passou aqui {contador} vezes. - Nota errada, erro de digitar')
        contador += 1
