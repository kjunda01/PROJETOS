
'''
For / Else em Python
'''
import os

variavel = os.listdir('/home/kjunda01/Desktop/PROJETOS/Testes')

# variavel = ['Sinval', 'Giovana', 'Samuel']

# for nome in variavel:
#     print(nome)
#     #break
#     #continue
#     print(nome)


for valor in variavel:
    if valor.endswith('.zip'):
        listazips = [valor.endswith('.zip')]
        print(listazips)
    else:
        print('NÃO ---> .zip', valor)
