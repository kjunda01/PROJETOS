secreto = 'giovana'
digitadas = []
chances = 3

while chances > 0:
    letra = input('Digite uma letra: ').lower()  # Converta a letra para minúscula

    if not letra.isalpha() or len(letra) != 1:
        print('Digite uma única letra do alfabeto.')
        continue

    if letra in digitadas:
        print(f'Você já digitou a letra "{letra}".')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe.\n')
    else:
        print(f'A letra "{letra}" NÃO EXISTE!.\n')

    secreto_temp = ''.join([letra_secreta if letra_secreta in digitadas else '*' for letra_secreta in secreto])

    if secreto_temp == secreto:
        print(f'Muito bem, você adivinhou a palavra {secreto_temp}!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}.')

    if letra not in secreto:
        chances -= 1

    if chances > 0:
        print(f'Você ainda tem {chances} chances.')

if chances == 0:
    print(f'Acabaram suas chances. A palavra secreta era: {secreto}.')
