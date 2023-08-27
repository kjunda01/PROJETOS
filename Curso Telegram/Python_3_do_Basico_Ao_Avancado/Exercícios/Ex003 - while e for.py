# Exercícios estrutura de repetição

'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

# NOME MAIOR QUE 3 CARACTERES
while True:
    nome = input('Digite um nome: ')
    if len(nome) < 3:
        print('Seu nome deverá ter, no mínimo, 3 caracteres. Tente novamente.')
    else:
        print(f'{nome}, nome cadastrado com sucesso.')
        break


# IDADE ENTRE 0 E 150
while True:
    try:
        idade = int(input('Idade: '))
        if idade >= 0 and idade <= 150:
            print('Idade cadastrada com sucesso.')
            break
    except ValueError:
        print('Digite uma idade válida.')


# SALÁRIO MAIOR QUE R$00,00
while True:
    try:
        salario = float(input('Salário: R$'))
        if salario > 0:
            print('Salário cadastrado com sucesso.')
            break
    except ValueError:
        print('Dígito inválido, tente novamente.')


# GENERO SEXUAL M OU F
while True:
    cats_genero = ['M', 'F']
    genero = [input('Gênero: [M] ou [F]: ').upper()]
    if genero[0] in cats_genero:
        print('Gênero cadastrado com sucesso.')
        break
    else:
        print('Gênero errado. Tente novamente.')


# ESTADO CIVIL
while True:
    cats_estado_civil = ['S', 'C', 'V', 'D']
    estado_civil = [input('Estado Civil: [S], [C], [V] ou [D]: ').upper()]
    if estado_civil[0] in cats_estado_civil:
        print('Estado Civil cadastrado com sucesso.')
        break
    else:
        print('Estado civil errado. Tente novamente.')


print(f'\n*** Dados do usuário ***\n'
      f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salário: R${salario}\n'
      f'Gênero: {genero[0]}\n'
      f'Estado Civil: {estado_civil[0]}\n')
