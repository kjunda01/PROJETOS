# O que o código deverá fazer:
# 4 - Listar todos os arquivos dentro da pasta destino
# 5 - Extrair todos os arquivos .zip dentro da pasta
# 6 - Verificar novamente todos os arquivos dentro da pasta
# 7 - Renomear todos os arquivos com extensão .jpeg e .JPG para o nome da pasta
# (considerar os 30 primeiros caracteres) + SITE na frente

# Bibliotecas
import os
import shutil

# 2 - Copiar o "É NOTÍCIA - MODELO.cdr" para o diretorio atual
def copiar_enoticia():
    noticia = "/home/kjunda01/OneDrive 2s1xlx/SEMED 2020/COMUNICAÇÃO PREFEITURA/Publicações/Modelo para publicação/Modelo/É NOTÍCIA - MODELO.cdr" # Localização real do arquivo modelo
    modelo = "É NOTÍCIA - MODELO.cdr" # Nome do arquivo .cdr para fazer a cópia e checagem
    pasta = os.getcwd()
    caminho_final_modelo = os.path.join(pasta, modelo)

    if os.path.exists(caminho_final_modelo):
        print(f'\nArquivo "{modelo}" presente da pasta, pulando etapa.\n')
    else:
        print(f'\n"{modelo}" -----> "{pasta}"')
        shutil.copy2(noticia, pasta)
        print('\nCópia concluída com sucesso.\n')

# 3 - Renomear o "É NOTÍCIA - MODELO.cdr" para os 30 primeiros caracteres do caminho final modelo
def renomear_enoticia():
    pasta = os.getcwd()
    print('Renomeando arquivo ".cdr" para o nome da pasta atual.....\n')
    caminho_antigo = os.path.join(pasta, "É NOTÍCIA - MODELO.cdr")
    # /home/kjunda01/Desktop/PROJETOS/Testes/É NOTÍCIA - MODELO.cdr
    caminho_novo = pasta[32:61] + '.cdr'
    # /home/kjunda01/Desktop/PROJETOS/Testes/
    os.rename(caminho_antigo, caminho_novo)

# 4 - Listar zips
zips = [arq for arq in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), arq)) and arq.endswith(".zip")]

# 5 - Extrair zips
# for zip_file in listar_zips():
#     caminho_zip = os.path.join(os.getcwd(), zip_file)
#     shutil.unpack_archive(caminho_zip, os.getcwd())
#     print('Arquivo ".zip" extraído com sucesso.\n')

copiar_enoticia()
renomear_enoticia()
print(zips)
