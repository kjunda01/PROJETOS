"""
Operador ternário em Python

"""

# from getpass import getuser

# logged_user = False

# if logged_user:
#     msg = f'Olá, {getuser()}. Você está logado.'
# else:
#     msg = 'Usuário precisa logar.'

# print(msg)


# logged_user = True

# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

# print(msg)

idade = 17
maior_de_idade =  idade >= 18

confirma = 'Pode acessar.' if idade >= 18 else 'Não pode acessar.'

confirma2 = 'Pode.' if maior_de_idade else 'Não pode.'

print()
print(confirma)
print()
print(confirma2)

