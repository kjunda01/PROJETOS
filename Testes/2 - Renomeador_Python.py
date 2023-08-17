import os
import os.path
from pathlib import PurePath
import shutil
import glob

enoticia = '/home/kjunda01/Downloads/É NOTÍCIA - MODELO.cdr'
diretorio_padrao = os.getcwd()
# COPIAR O ARQUIVO .CDR FEITO E OK


# if os.path.isfile(shutil.copy2(enoticia, diretorio_padrao)):
#     print(
#         f'\nArquivo "{shutil.copy2(enoticia, diretorio_padrao)[-22:]}" já está na pasta {diretorio_padrao[diretorio_padrao.rfind("/"):]}')
#     print(f'{diretorio_padrao}')
#     print('Pulando etapa...\n')
# else:
#     print('Copiando....')


# Detectar quantos arquivos cdr estão no diretorio padrão
achar_cdr = glob.glob('*.cdr')

contador = 1

for cdrs in achar_cdr:
    print(cdrs)
    print(diretorio_padrao)

    # print(novo_nome_cdrs)
    # direct = os.path.basename(os.path.dirname(diretorio_padrao))
    # print(direct)
    # antigo_nome_cdrs = diretorio_padrao + '/' + cdrs
    # print(antigo_nome_cdrs)
    # # print(nome_antigo_cdrs)

    # print(novo_nome_cdrs)

    # nome_novo_cdrs = os.rename(nome_antigo_cdrs, diretorio_padrao.removeprefix(diretorio_padrao)+'.cdr')
    # print(nome_novo_cdrs)
