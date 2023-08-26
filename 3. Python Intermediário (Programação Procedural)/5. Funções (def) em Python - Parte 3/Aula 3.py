'''
Funções (def) em Python - *args **kwargs
'''

# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6

# var = func(1, 2, 3, 4, 5, nome='Sinval', a6='26')

def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1, 2, 3, 4, 5)
