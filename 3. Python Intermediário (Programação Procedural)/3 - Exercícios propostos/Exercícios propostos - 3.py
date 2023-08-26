"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo é um
percentual (Ex. 10%). Retorne (return) o valor do primeiro número somado ao aumento
do percentual do mesmo.
"""
# from getpass import getuser
# usuario = getuser()

# while True:
#     try:
#         percent = float(input('Digite a porcentagem: '))
#         break
#     except ValueError:
#         print('Digite somente números!')
# while True:
#     try:
#         valor = float(input('Digite um número: '))
#         valorperc = (percent / 100) * valor
#         break
#     except ValueError:
#         print('Digite somente números!')



# def percentagem(montante, porcentagem):
#     return montante + porcentagem


# porcentagem = percentagem(valor, (valorperc+valor))
# print(f'{usuario}, {percent:.2f}% de {valor:.2f} é {valorperc:.2f}.\n'
#       f'{valorperc:.2f} + {valor:.2f} = {valor + valorperc:.2f}')


def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)
