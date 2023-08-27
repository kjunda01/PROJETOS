"""
1 - Crie uma função que exiba uma saudação com os parâmetros 'saudacao' e 'nome'.
"""

from getpass import getuser

usuario = getuser()


def saudacao(saudacao, nome):
    print('Testando...')
    print(f'{saudacao}, {nome}')

saudacao('', '' )
saudacao('Olá', usuario)
saudacao('Opa', 'Kjunda' )
