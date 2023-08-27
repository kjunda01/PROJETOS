"""
4 - Fizz Buzz -  Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, renorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne
o número enviado.
"""
from random import randint

def fb(numero):
    
    if numero % 3 == 0 and numero % 5 == 0:
        return f'FizzBuzz, {numero} é divisível por 3 e 5.'
    
    if numero % 5 == 0:
        return f'Buzz, {numero} é divisível por 5.'
    
    if numero % 3 == 0:
        return f'Fizz, {numero} é divisível por 3.'
    
    return numero
    

for sequencia in range(100):
    aleatorio = randint(0,100)
    print(fb(aleatorio))
