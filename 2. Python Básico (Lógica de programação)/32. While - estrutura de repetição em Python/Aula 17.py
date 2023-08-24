'''
While em Python - Aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores

'''


# while True:
#     nome = input('Qual é o seu nome? ')
#     print(f'Olá, {nome}!')
#     #continue
#     # Sempre que tiver a palavra continue ele vai parar de executar todos os outros comandos posteriores
#     print(f'Olá1, {nome}!')
#     print(f'Olá2, {nome}!')
#     print(f'Olá3, {nome}!')
#     print(f'Olá4, {nome}!')
#     print(f'Olá5, {nome}!')
#     print(f'Olá6, {nome}!')
#     print(f'Olá7, {nome}!')
#     print(f'Olá8, {nome}!')
    #break
    # Sempre que tiver a palavra break ele para o loop e vai para o proximo passo


# x = 0 # coluna
# while x < 10:
#     y = 0 # linha

#     while y < 5:
#         print(f'({x},{y})')
#         y += 1 # y = y + 1
    
#     x += 1

# print('Acabou!')    

# Primeiro número para a conta
while True:
    try:
        num1 = float(input('\nPrimeiro número: '))
        break
    except ValueError:
        print("Valor inválido. Insira um número válido.")

# Operadores, com mensagem inicial e depois corrigindo erros
print('\nOperadores:\n'
    'Adição -------------> (+)\n' 
    'Subtração ----------> (-)\n'
    'Multiplicação ------> (*)\n' 
    'Divisão ------------> (/)\n' 
    'Exponenciação ------> (**)')
operador = input('\nDigite o operador: ')
lista_operador = ("+", "-", "*", "/", "**")
while operador not in lista_operador:
    operador = input('\nLOOP - Digite o operador: ')

# Segundo número para a conta
while True:
    num2 = input('\nSegundo número: ')
    if num2.isnumeric():
        num2 = float(num2)
        break

# Resultado da calculadora:
print("\nMuito bem, vamos ao cálculo:\n")
if operador == "+":
    print(f'{num1} + {num2} = {num1 + num2}\n')
elif operador == "-":
    print(f'{num1} - {num2} = {num1 - num2}\n')
elif operador == "*":
    print(f'{num1} x {num2} = {num1 * num2}\n')
elif operador == "/":
    print(f'{num1} / {num2} = {num1 / num2}\n')
elif operador == "**":
    print(f'{num1} elevado a {num2} = {num1 ** num2}\n')
