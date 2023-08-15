"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

# BIBLIOTECA:
from datetime import datetime

# APRESENTAÇÃO:
print(f'Olá, seja bem vindo(a) ao nosso desafio prático')
nome = input(f'Para começar, me informe seu nome: ')
print(f'Muito bem {nome}, vamos ao que interessa ao nosso desafio.')

# COLETA DE DADOS:
idade = int(input('Me fale sua idade: '))
#idade = int(anos_de_vida)
altura = float(input('Me fale agora sua altura, em metros: '))
#altura = float(medicao)
peso = float(input('Por último, me informe seu peso, em quilogramas: '))
#peso = int(pesagem)
ano = int(datetime.now().year)
nascimento = ano-idade
imc = peso / altura**2

# CÁLCULO DO IMC:
if imc <= 18.50:
    imc_resp = f'Com o imc de {imc:.2f} você se encaixa em: Magreza.'
elif imc <= 24.99:
    imc_resp = f'Com o imc de {imc:.2f} você está na categoria Normal.'
elif imc <= 29.99:
    imc_resp = f'Com o imc de {imc:.2f} você está no Sobrepeso - Obesidade Grau I'
elif imc <= 39.99:
    imc_resp = f'Com o imc de {imc:.2f} você pertence à categoria Obesidade - Grau II'
elif imc >= 40:
    imc_resp = f'Com o imc de {imc:.2f} você pertence à categoria Obesidade Grave - Grau III'

# INFORMANDO TODOS OS DADOS COLETADOS:
print(f'Muito bem, {nome}, vamos as respostas.')
print(f'Com a idade de {idade} anos, você nasceu em {int(nascimento)} e está atualmente com o imc de {imc:.2f}. {imc_resp}')
print('Pasaremos agora para as informações dos dados coletados.')
print(f'{type(idade)} foi o tipo da idade.')
print(f'{type(altura)} foi o tipo da altura')
print(f'{type(peso)} foi o tipo do peso.')

# FINALIZANDO O SCRIPT
print()
print(f'{nome}, foi um prazer. Espero te ver mais aqui! Tchau!')
