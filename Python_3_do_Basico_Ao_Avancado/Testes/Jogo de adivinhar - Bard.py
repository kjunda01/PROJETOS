secreto = 'giovana'
digitadas = []
chances = 3

def mostrar_palavra(secreto, digitadas):
    palavra_revelada = ''
    for letra in secreto:
        if letra in digitadas:
            palavra_revelada += letra
        else:
            palavra_revelada += '*'
    return palavra_revelada

while chances > 0:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Opa, digite somente UMA letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe.\n')
        secreto = secreto.replace(letra, '*' * secreto.count(letra))
    else:
        print(f'A letra "{letra}" NÃO EXISTE!.\n')
        digitadas.pop()

    palavra_revelada = mostrar_palavra(secreto, digitadas)

    if palavra_revelada == secreto:
        print(f'Muito bem, você adivinhou a palavra {secreto}!!')
        break

    if chances > 0:
        print(f'A palavra secreta está assim: {palavra_revelada}.')
        print(f'Você ainda tem {chances} chances.')

if chances == 0:
    print('Você perdeu!')
