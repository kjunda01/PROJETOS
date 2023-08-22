# BIBLIOTECAS NECESSARIAS
import os
import shutil
import glob

# VARIÁVEIS INICIAIS
main_folder_path = os.getcwd()
main_folder_only = os.getcwd().split('/')[-1]


# ********** COMEÇO DO PROGRAMA **********

# EXTRAIR OS ARQUIVOS ZIP
def zip_extract():
    print('Extraindo arquivos .zip..')
    zip_list = glob.glob('*.zip')
    for zips in zip_list:
        shutil.unpack_archive(zips)
        print(f'Arquivo "{zips}" extraído com sucesso.')


# COPIAR O É NOTICIA PARA O WORKING DIRECTORY
def copy_cdr():
    e_noticia_folder = '/home/kjunda01/Downloads/É NOTÍCIA - MODELO.cdr'
    print(f'Copiando arquivo "{e_noticia_folder.split("/")[-1]}" para a pasta "{main_folder_only}".')
    shutil.copy2(e_noticia_folder, main_folder_path)

# FUNÇÕES DE RENOMEAR ARQUIVOS
def rename_cdr():
    dir_list = glob.glob('*')
    counter_cdr = 1
    for files in dir_list:
        file_extention = f'.{files.split(".")[-1]}'
        old_file_name = main_folder_path + '/' + files

        # RENOMEAR CDR
        if file_extention.endswith('.cdr'):
            new_name_only_cdr = f'É NOTÍCIA - {main_folder_only[:30]}({counter_cdr}){file_extention}'
            new_path_cdr = os.path.join(main_folder_path, new_name_only_cdr)
            if not os.path.exists(new_path_cdr):
                os.rename(old_file_name, new_path_cdr)
                print(f'"{files}" ----> "{new_name_only_cdr}".')
                counter_cdr += 1


def rename_jpeg():
    dir_list = glob.glob('*')
    counter_jpeg = 1
    for files in dir_list:
        file_extention = f'.{files.split(".")[-1]}'
        old_file_name = main_folder_path + '/' + files

        # RENOMEAR JPEG
        if file_extention.endswith('.jpeg'):
            new_name_only_jpeg = f'É NOTÍCIA - {main_folder_only[:30]} - SITE({counter_jpeg}){file_extention}'
            new_path_jpeg = os.path.join(main_folder_path, new_name_only_jpeg)
            if not os.path.exists(new_path_jpeg):
                os.rename(old_file_name, new_path_jpeg)
                print(f'"{files}" ----> "{new_name_only_jpeg}".')
                counter_jpeg += 1


def rename_zip():
    dir_list = glob.glob('*')
    counter_zip = 1
    for files in dir_list:
        file_extention = f'.{files.split(".")[-1]}'
        old_file_name = main_folder_path + '/' + files

        # RENOMEAR ZIP
        if file_extention.endswith('.zip'):
            new_name_only_zip = f'{main_folder_only[:30]} - ZIP({counter_zip}){file_extention}'
            new_path_zip = os.path.join(main_folder_path, new_name_only_zip)
            os.rename(old_file_name, new_path_zip)
            print(f'"{files}" ----> "{new_name_only_zip}".')
            counter_zip += 1

copy_cdr()
zip_extract()
rename_cdr()
rename_jpeg()
rename_zip()

# MENSAGEM FINAL
print('Tarefas concluídas com successo!')
