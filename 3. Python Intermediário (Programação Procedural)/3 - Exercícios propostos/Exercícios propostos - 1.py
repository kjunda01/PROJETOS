"""
1 - Crie uma função que exiba uma saudação com os parâmetros 'saudacao' e 'nome'.
"""

from getpass import getuser

usuario = getuser()


def saudacao(saudacao='Olá', nome=usuario):
    print('Testando...')
    print(saudacao, nome)


saudacao()

