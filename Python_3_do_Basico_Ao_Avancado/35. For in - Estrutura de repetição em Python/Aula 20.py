'''
Enquanto o contador for menor que o tamanho da frase (34)
    a letra será igual a frase[começando com 0]
    se a letra for igual ao input do usuario:
        a nova string é igual a nova string + o input do usuário em maiúsculo
    se nao:
        nova string é igual a nova string mais letra
    # depois disso tudo temos que adicionar o contador, para fazer a iteração:
    contador é igual ao contador + um.
'''


"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
"""


# o while é utilizado quando nao se sabe o fim.


# o laço for é utilizado quando se sabe o que vai finalizar, tipo uma contagem, tipo uma tabuada de 0 a 10

# texto = 'Eu estou gostando de aprender Python'
# contador = 0

# while contador < len(texto):
#     print(texto[contador])
#     contador += 1

# texto = 'Python'

# for letra in texto:
#     print(letra)

# for numero in range(0, 10, 2):
#     print(numero)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)