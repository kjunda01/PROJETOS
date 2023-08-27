# Tenta fazer esse Problema: O custo ao consumidor de um carro novo é:
# A soma do custo de fábrica com a percentagem do revendedor e com o custo dos impostos (aplicados ao custo de fábrica).
# Supondo que a percentagem do revendedor seja de 25% do custo de fábrica
# e que os impostos custam 45 % do custo de fábrica,
# faça um algoritmo que leia o valor de custo de fábrica e determine o preço final do automóvel (custo ao consumidor).



# Forma antiga
# while True:
#     usuario_custo_fabrica = input("Quanto a loja anuncia o preço de fábrica do veículo? ")
#     if usuario_custo_fabrica.isdigit():
#         usuario_custo_fabrica = float(usuario_custo_fabrica)
#         break

#Valor inicial do veículo
# Forma nova de tratar os erros:
while True:
    try:
        usuario_custo_fabrica = float(input("Quanto a loja anuncia o preço de fábrica do veículo? "))
        break
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

#Valor dos impostos
impostos = 45/100 * usuario_custo_fabrica

#Valor do custo do veículo
custo_veiculo = usuario_custo_fabrica - impostos

# Percentagem do revendedor
perc_revendedor = 25/100 * usuario_custo_fabrica

# Custo final
custo_final = usuario_custo_fabrica + perc_revendedor + impostos

# Apresentação dos resultados:
print(f"\n**********************  EXTRATO  ********************")
print(f"Valor do custo de fábrica:**************-> R${usuario_custo_fabrica:.2f}.")
print(f"Valor real para produzir: **************-> R${custo_veiculo:.2f}.")
print(f"Valor dos impostos: ********************-> R${impostos:.2f}.")
print("                                           ----------")
print(f"O custo final foi de: ******************-> R${custo_final:.2f}.\n")

