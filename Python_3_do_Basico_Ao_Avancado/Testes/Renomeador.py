# O que o código deverá fazer:
# 4 - Listar todos os arquivos dentro da pasta destino
# 5 - Extrair todos os arquivos .zip dentro da pasta
# 6 - Verificar novamente todos os arquivos dentro da pasta
# 7 - Renomear todos os arquivos com extensão .jpg e .JPG para o nome da pasta (considerar os 30 primeiros caracteres) + SITE na frente
# 8 - 

# Bibliotecas
from getpass import getuser
import os
from shutil import copy2

# 1 - Variáveis iniciais
diretorio_atual = os.getcwd()
usuario = getuser()

# 2 - Copiar o "É NOTÍCIA - MODELO.cdr" para o diretorio atual
noticia = "/home/kjunda01/OneDrive 2s1xlx/SEMED 2020/COMUNICAÇÃO PREFEITURA/Publicações/Modelo para publicação/Modelo/É NOTÍCIA - MODELO.cdr" # Localização real do arquivo modelo
modelo = "É NOTÍCIA - MODELO.cdr" # Nome do arquivo .cdr para fazer a cópia e checagem
caminho_final_modelo = os.path.join(diretorio_atual, modelo)

while True:
    try:
        copiar_enoticia = int(input(f'{usuario}, deseja copiar "É NOTÍCIA - MODELO.cdr" para a pasta "{diretorio_atual}"? [1]SIM - [2]NÃO  ')) # modificar o diretorio atual
        if copiar_enoticia == 1:
            if os.path.exists(caminho_final_modelo):
                print(f'Arquivo "{modelo}" presente da pasta, pulando etapa.\n')
                break
            else:
                print(f'"{modelo}" -----> "{diretorio_atual}"')
                copy2(noticia, diretorio_atual)
                print('Cópia concluída com sucesso.')
                break
        if copiar_enoticia == 2:
            print('Continuando...')
            break
    except ValueError:
        print('Dígito errado, selecione as opções corretas.\n[1]SIM - [2]NÃO')

# 3 - Renomear o "É NOTÍCIA - MODELO.cdr" para os 30 primeiros caracteres do caminho final modelo
os.rename(caminho_final_modelo, diretorio_atual[32:61]+'.cdr')
# O que o código deverá fazer:
# 4 - Listar todos os arquivos dentro da pasta destino
# 5 - Extrair todos os arquivos .zip dentro da pasta
# 6 - Verificar 