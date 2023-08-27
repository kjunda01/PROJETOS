"""

Funções - def em Python (Parte 1)

"""

# def saudacao(msg='Olá', nome='usuário'):
#     print(msg, nome)

# saudacao('Opa', 'Moab')
# saudacao('','')

from getpass import getuser
def saudacao(msg='Olá', nome=getuser()):
    nome = nome.replace('E', '3')
    msg = msg.replace('á', '@')
    return f'{msg}, {nome}'

variavel = saudacao()
print(variavel)