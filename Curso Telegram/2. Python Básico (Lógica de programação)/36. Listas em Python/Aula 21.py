"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# Valores positivos
#         0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1
# Valores negativos

#  Desafio
# Faça um jogo de adivinhar onde as pessoas podem descobrir qual é a minha palavra secreta

secreto = 'giovana'
digitadas = []
chances = 3

while True:
    if chances < 1:
        # print('Acabaram suas chances. Que pena!')
        print('Você perdeu!')
        break

    letra = input('\nDigite uma letra: ')

    if len(letra) > 1:
        print('Opa, digite somente UMA letra.\n')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'"{letra}" existe.\n')
    else:
        print(f'A letra "{letra}" NÃO EXISTE!.\n')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Muito bem, você adivinhou a palavra {secreto_temp}!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}.')

    if letra not in secreto:
        chances -= 1

    if chances > 0:
        print(f'Você ainda tem {chances} chances.')

print
