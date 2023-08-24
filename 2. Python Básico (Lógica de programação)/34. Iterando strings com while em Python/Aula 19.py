# 34. Iterando strings com while em Python
# índices
# 0123456789.......................33

frase = "O rato roeu a roupa do rei de roma"
tamanho_frase = len(frase)
contador = 0

nova_string = ''

while True:
    try:
        input_do_usuario = input('Qual letra deseja colocar maiúscula? ')
        if input_do_usuario in frase and input_do_usuario != " " and input_do_usuario != '':
            break
    except ValueError:
        print('Digite apenas os caracteres da frase: O rato roeu a roupa do rei de roma')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)


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