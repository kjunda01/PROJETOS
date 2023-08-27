# função len

# Só funciona com string.

usuario = input(f'Digite seu ususário: ')
qtd_caracteres = len(usuario)
print(f'Seu usuário é "{usuario}" e ele possui "{len(usuario)}" caracteres, com o tipo de dado sendo da {type(qtd_caracteres)}')