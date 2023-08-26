'''
Funções (def) em Python - *args **kwargs
'''

from random import randint

aleatorio = randint(0,100)

def func(a1, a2, a3, a4, a5):
    
    print(a1, a2, a3, a4, a5)

func(randint(0,100), randint(0,100), randint(0,100), randint(0,100),  randint(0,100))
