'''
Iniciar com letra, pode conter números, separar _, letras minúsculas

'''

# Fazer exercício de IMC
# para realizar divide-se o peso (em kg) pelo quadrado da altura (em metros).

# Apresentação
print(f'Olá, seja bem-vindo(a)')
nome = input(f'Qual o seu nome? ')

# Coletar dados
print(f'{nome}, vou te pedir alguns dados.')

pesagem = input('Me diga seu peso, em kg: ')

medicao = input('Agora, me diga sua altura, em metros: ')

altura = float(medicao)
peso = float(pesagem)

# Realizar o cálculo
imc = peso / altura ** 2

if imc <= 18.50:
    resp = (f'você se encaixa na categoria Magreza.')
elif imc <= 24.99:
    resp = (f'você se encaixa na categoria Normal.')
elif imc <= 29.99:
    resp = (f'você se encaixa na categoria Sobrepeso - Obesidade I.')
elif imc <= 39.99:
    resp = (f'você se encaixa na categoria Obesidade II.')
elif imc >= 40.0:
    resp = (f'você se encaixa na categoria Obesidade Grave - Grau III.')


# Apresentar os resultados
print(f'{nome}, com uma massa de {peso}Kg e altura de {altura}m {resp}, com o imc {imc:.2f}.')
