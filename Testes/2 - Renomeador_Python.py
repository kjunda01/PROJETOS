import os
import shutil
import glob


diretorio_padrao = os.getcwd()


def copiar_cdr():
    # COPIAR O ARQUIVO .CDR FEITO E OK
    enoticia = '/home/kjunda01/Downloads/É NOTÍCIA - MODELO.cdr'
    verificar_cdr = glob.glob('*.cdr')
    if not verificar_cdr:
        shutil.copy2(enoticia, diretorio_padrao)
    else:
        print('\nArquivo .cdr já está na pasta. Pulando etapa...\n')


def renomear_cdr():
    # Detectar quantos arquivos cdr estão no diretorio padrão
    achar_cdr = glob.glob('*.cdr')

    # Variável para acrescentar um contador
    contador = ''

    for cdrs in achar_cdr:
        # Acha qual o antigo nome do cdr
        antigo_nome_cdr = os.path.join(diretorio_padrao, cdrs)

        # Acha qual o nome da pasta atual, somente ela.
        pasta_local = diretorio_padrao.split("/")[-1]

        # Acha o nome do arquivo considerando apenas os 30 caracteres da pasta
        nome_30 = os.path.join(
            'É NOTÍCIA - ' + pasta_local[0:30] + contador + '.cdr')

        # Define como vai ser o novo nome do arquivo cdr
        novo_nome_cdr = os.path.join(diretorio_padrao, nome_30)

        # Renomeia os arquivos para o novo nome
        os.rename(antigo_nome_cdr, novo_nome_cdr)

        # Variavel para somar uma letra ao final, para conseguir renomear varios arquivos.
        contador += '-'


def nomes_dos_arquivos():
    # Verificar os arquivos dentro da pasta em que o script está rodando
    for arquivos in glob.glob('*'):

        # Diretorio da pasta em que o script está rodando
        diretorio = os.getcwd()

        # Caminho completo dos arquivos da pasta
        caminho_antigo_nome = os.path.join(diretorio, arquivos)

        # Conseguir extensão dos arquivos para acrecentar nos que não possuem devido ao limite de 30 caracteres
        extensao = '.' + arquivos.split(".")[-1]

        # Nome com extensão dos arquivos na pasta
        arquivos_pasta_local = arquivos.split("/")[-1]

        # Checar se o nome já tem a extensão
        if extensao in arquivos_pasta_local[0:30]:
            # se já tiver não fará nada
            print(os.path.join(diretorio, arquivos_pasta_local[0:30]))
        else:
            # Se não tiver vai acrescentar a extensão ao arquivo
            adicionar_extensao = arquivos_pasta_local[:30] + extensao
            novo_arquivo_30 = os.path.join(diretorio, adicionar_extensao)
            print(novo_arquivo_30)


copiar_cdr()
renomear_cdr()
nomes_dos_arquivos()

