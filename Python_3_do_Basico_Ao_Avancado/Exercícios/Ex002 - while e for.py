# Exercícios estrutura de repetição

'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

# contador = 1

# while True:
#     try:
#         print(
#             f'Você já passou aqui {contador} vezes. - Try')
#         contador += 1
#     except ValueError:
#         print(
#             f'Você já passou aqui {contador} vezes. - Except')
#         contador += 1


while True:

    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if senha == usuario:
        print('A senha não pode ser igual ao usuário, tente novamente.')
    else:
        print('Cadastro realizado com sucesso.')
        break

print('Bem vindo(a) ao sistema.')
