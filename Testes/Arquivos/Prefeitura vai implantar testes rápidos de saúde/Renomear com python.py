# BIBLIOTECAS NECESSARIAS
import os
import shutil
import glob
from time import sleep

# VARIÁVEIS INICIAIS
main_folder_path = os.getcwd()
main_folder_only = main_folder_path.split('/')[-1]
dir_list = glob.glob('*')
zip_list = glob.glob('*.zip')

# CONTADORES
counter_cdr = 1
counter_jpeg = 1
counter_png = 1
counter_zip = 1


# ********** COMEÇO DO PROGRAMA **********

# EXTRAIR OS ARQUIVOS ZIP
print('Extraindo arquivos .zip...')
for zips in zip_list:
    shutil.unpack_archive(zips)


# COPIAR O É NOTICIA PARA O WORKING DIRECTORY
print('Copiando arquivo .cdr para a pasta...')
e_noticia_folder = '/home/kjunda01/Downloads/É NOTÍCIA - MODELO.cdr'
shutil.copy2(e_noticia_folder, main_folder_path)


# RENOMEANDO OS ARQUIVOS
print('Reomeando arquivos...')
for files in dir_list:
    file_extention = f'.{files.split(".")[-1]}'
    old_file_name = main_folder_path + '/' + files
    
    # RENOMEAR CDR
    if file_extention.endswith('.cdr'):
        new_name_only_cdr = f'É NOTÍCIA - {main_folder_only[:30]}({counter_cdr}){file_extention}'
        new_path_cdr = os.path.join(main_folder_path, new_name_only_cdr)
        if not os.path.exists(new_path_cdr):
            os.rename(old_file_name, new_path_cdr)
            counter_cdr += 1


    # RENOMEAR JPEG
    if file_extention.endswith('.jpeg'):
        new_name_only_jpeg = f'É NOTÍCIA - {main_folder_only[:30]} - SITE({counter_jpeg}){file_extention}'
        new_path_jpeg = os.path.join(main_folder_path, new_name_only_jpeg)
        if not os.path.exists(new_path_jpeg):
            os.rename(old_file_name, new_path_jpeg)
            counter_jpeg += 1


    # RENOMEAR ZIP
    if file_extention.endswith('.zip'):
        new_name_only_zip = f'{main_folder_only[:30]} - ZIP({counter_zip}){file_extention}'
        new_path_zip = os.path.join(main_folder_path, new_name_only_zip)
        os.rename(old_file_name, new_path_zip)
        counter_zip += 1


# MENSAGEM FINAL
print('Tarefas concluídas com successo!')

