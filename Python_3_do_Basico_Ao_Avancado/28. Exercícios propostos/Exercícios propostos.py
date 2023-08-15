"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex: Bom dia 0h as 11h, boa tarde 12h as 17h, e Boa noite 18h as 23h
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; 
se tiver entre 5 e 5 letras, escreva "Seu nome é normal"; maior que 6, escreva "Seu nome é muito grande."
"""

# Biblioteca para pegar o nome do usuário
import getpass # Essa biblioteca retorna o “nome de login” do usuário.

# Começo do programa
print("*" * 181)
nome = input('Para começarmos, digite seu primeiro nome: ')
nome = nome or getpass.getuser()
# se o usuário não digitar nada, consideraremos o nome como Usuário.

# Prosseguindo...
print(f"Muito bem {nome}, iniciaremos o programa.")
print()

# Definindo as funções para chamar posteriormente

# Função do exercício 1
def exercicio1():
    # Pede o numero inteiro
    num_int = input(f"Agora, {nome}, digite um número inteiro, por gentileza: ")
    numero_inteiro = num_int.isdigit()
    
    # Verifica se é numero inteiro e só permite passar para o proximo se for inteiro.
    if not numero_inteiro:
        num_int = input("Digite apenas um número inteiro: ")
        numero_inteiro = num_int.isdigit()
        while numero_inteiro != True:
            num_int = input("Digite APENAS um número inteiro, por favor: ")
            numero_inteiro = num_int.isdigit()
                
    # Se passar do teste de somente um numero inteiro ele verifica se é par ou ímpar.   
    num_int = int(num_int)    
    if num_int % 2 == 0:
        print(f'{nome}, o número "{num_int}" que você digitou é PAR.')
    else:
        print(f"O número {num_int} é ÍMPAR.")


# Função do exercício 2
def exercicio2():
    hora = input(f"{nome}, me informe uma hora (somente números): ")
    hrs = hora.isnumeric()
    
    # Confere se as horas são numeros de horas
    if not hrs:
        hora = input("Digite somente números correspontentes a horas: ")
        hrs = hora.isnumeric()
        
        # Mantem a checagem até sair um numero certo
        while not hrs:
            hora = input("Digite APENAS números correspontentes a horas: ")
            hrs = hora.isnumeric()
            
    # Converter novamente a hora para checarmos o numero
    hora = int(hora)
    
    # Agora vamos a saudação apropriada
    if hora < 0:
        print('Infelizmente horas negativas ainda não são suportadas.')
    elif hora <= 6:
        print("Está ainda de madrugada, tenha uma boa noite!")
    elif hora <= 12:
        print("De manhãnzinha, que beleza. Bom dia!")
    elif hora <= 18:
        print("Estou sentindo cheiro de café? Boa tarde!!")
    elif hora <= 23:
        print(f"Bons sonhos, {nome}, boa noite..")
    else:
        print("Que dia cheio ein? Horas acima de 24h não existem em meu sistema.")


# Função do exercício 3
def exercicio3():
    verificar_nome = len(nome)
    if verificar_nome <= 4:
        print(f'{nome}, que nome curto, somente {verificar_nome} caracteres.')
    elif verificar_nome < 6:
        print(f'{nome}, seu nome é de tamanho normal, contendo estes {verificar_nome} caracteres.')
    else:
        print(f'{nome}, que nome grande é o seu, com {verificar_nome} caracteres.')


# Chamando as funções na ordem em que o exercício está rodando:
exercicio1()
exercicio2()
exercicio3()

# Final do programa
print(f"{nome}, encerraremos o programa por aqui. Muito obrigado!")
print("*" * 181)