#Falaremos hoje sobre a função print

#print("Opa")


# o que está após a função print são seus argumentos.

#print("Argumento 1", "Argumento 2")

# colocaremos mais um argumento, agora o sep

#print("Sinval", "Junior", sep=(' *-* '))

#print("João", "e", "Maria", sep=('---'))

#print(" 123,", "456, certo?", sep='-*-*', end='**********',)

# Utilizar a função print e separador, criar uma máscara para os CPFs

nome = print(input("Olá, qual seu nome? "))

print(f'Muito bem, {nome}. Qual seu CPF? Digite apenas números.')
cpf = input("CPF: ")
#cpf = ("")
print(f"Muito bem, seu cpf então é {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")
