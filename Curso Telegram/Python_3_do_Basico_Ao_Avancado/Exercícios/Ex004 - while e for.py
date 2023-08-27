# Exercícios estrutura de repetição

'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
'''

tempo = 1
a = 80000 * (1 + 0.0025) ** tempo
b = 200000 * (1 + 0.00125) ** tempo
while a < b:
    print(f'\n***************** Ano {tempo: ^} *****************')
    a = 80000 * (1 + 0.03) ** tempo
    b = 200000 * (1 + 0.015) ** tempo
    print('População da cidade A:', f'{a:.0f}'[
          :3] + '.' + f'{a:.0f}'[3:] + ' habitantes.')
    print('População da cidade B:', f'{b:.0f}'[
          :3] + '.' + f'{b:.0f}'[3:] + ' habitantes.')
    tempo += 1

print('\nResposta:')
print(f'Anos corridos para a Cidade A passar a Cidade B: {tempo-1} anos.')
