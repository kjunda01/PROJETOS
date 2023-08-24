# Documentação

'''
Teste com validação de numeros
'''

teste = str(-1.0)
print(teste.isalnum())
print(teste.isalpha())
print(teste.isascii())
print(teste.isdecimal())
print(teste.isnumeric())

# Nao vai funcionar porque o numero é numero negativo ou de ponto flutuante, verei mais pra frente. 

'''

# Pedido inicial
num1 = input("Digite um número: ")

# Vai passar o comando pra ver se pode ser numero
numero = num1.isalnum()
print(numero)

# Se conseguir ser numero, o programa finaliza, apresentando tres mensagens.
if numero == True:
    print("o if esta funcionando")
    print("Programa finalizado.")
    pass

# Se nao conseguir, ele vai entrar no loop pra poder verificar
else:
    print("o if nao funcionou")
    num1 = input("Digite novamente: ")
    numero = num1.isalnum()
    # Se aqui for numero, ele finaliza o programa.
    #Se nao for, ele entra no loop
    while numero != True:
        num1 = input("Mais uma vez: ")
        numero = num1.isalnum()
        # Se for número ele finaliza

# Mensagem final
print("Mensagem final")

'''

# Uma alternativa é utilizar o try e except, vamos la.


num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

try:
    # Se ele conseguir, vai mostrar a mensagem
    print("Vamos a conta: ")
    soma = float(num1) + float(num2)
    print(f"A soma é: {soma}")

except:
    print(f"{num1} + {num2} são imposíveis de se realizar a operação.")

