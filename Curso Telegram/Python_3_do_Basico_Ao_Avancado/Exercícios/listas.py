# Faça um programa que leia 5 números e informe o maior número.
'''
respostas = []
for indice in range(5):
    valor = float(input('Digite um número: '))
    respostas.append(valor)
    print(respostas)
    print(f'Valor {indice+1}')

maior_valor = max(respostas)
print(f'O maior valor digitado foi: {maior_valor}')
'''

# Exercício 1: Soma e Média
# Modifique o código para calcular a soma e a média dos valores
# digitados em vez de apenas encontrar o maior valor
# No final do loop, imprima a soma e a média.

# Exercício 2: Números Pares e Ímpares
# Após coletar os números, divida-os em duas listas: uma contendo os números pares
# e outra contendo os números ímpares. No final, imprima essas duas listas.

# Exercício 3: Valores Únicos
# Verifique se há valores repetidos na lista de respostas.
# Crie uma nova lista contendo apenas os valores únicos digitados pelo usuário.

# Exercício 4: Menor Valor
# Altere o código para encontrar tanto o maior quanto o menor valor na lista de respostas.

# Exercício 5: Valores Acima da Média
# Após calcular a média dos valores, crie uma lista que contenha apenas
# os valores que são maiores do que a média calculada. Imprima essa lista no final.

# Exercício 6: Limite de Valores
# Altere o código para permitir ao usuário definir um valor limite.
# O loop deve continuar coletando números até que o usuário digite um
# número maior do que o valor limite. Depois, exiba todos os números
# digitados e o valor máximo.

# Exercício 7: Manipulação de Strings
# Peça ao usuário para inserir strings em vez de números.
# Armazene as strings em uma lista e, no final, imprima todas as
# strings concatenadas em uma única string, separadas por vírgulas.

# Exercício 8: Ordenação Crescente
# Após coletar os valores, ordene-os em ordem crescente e imprima a lista ordenada.

# Exercício 9: Palíndromos
# Peça ao usuário para inserir palavras ou frases. Verifique se alguma das
# palavras/frases digitadas é um palíndromo (lê-se igual de trás para frente,
# desconsiderando espaços e pontuações).

# Exercício 10: Números Primos
# Crie uma função que verifica se um número é primo ou não. Ao final do loop,
# exiba os números primos digitados pelo usuário.

import getpass
usuario = getpass.getuser()

lista = []

for indice in range(3):
    pergunta = float(input(f'{usuario}, digite o algarismo ({indice+1}): '))
    lista.append(pergunta)

    # Exercício 1: Soma e Média
    count = 0
    for media in lista:
        count += 1
        media = sum(lista)/count




print(f'Números na lista: {lista}\n'  # Exercício 0
      f'Maior valor da lista: {max(lista)}\n'  # Exercício 0
      f'Menor valor da lista: {min(lista)}\n'  # Exercício 0
      f'Soma dos valores da lista: {sum(lista)}\n')  # Exercício 1: Soma e Média
#   f'Média dos valores da lista: {media:.2f}' # Exercício 1: Soma e Média
#   f'Números pares: {par}' # Exercício 2: Números Pares e Ímpares
#   f'Números ímpares: {impar}') # Exercício 2: Números Pares e Ímpares
