# BIBLIOTECAS NECESSARIAS
import os
import shutil
import glob

# VARIÁVEIS INICIAIS
main_folder_path = os.getcwd()

# ********** COMEÇO DO PROGRAMA **********

# EXTRAIR OS ARQUIVOS ZIP
print('Extraindo arquivos .zip..')
zip_list = glob.glob('*.zip')
for zips in zip_list:
    shutil.unpack_archive(zips)



# COPIAR O É NOTICIA PARA O WORKING DIRECTORY
e_noticia_folder = 'C:/Users/Kjunda01/OneDrive - 2s1xlx/SEMED 2020/COMUNICAÇÃO PREFEITURA/Publicações/Modelo para publicação/Modelo/É NOTÍCIA - MODELO.cdr'
shutil.copy2(e_noticia_folder, main_folder_path)

# FUNÇÕES DE RENOMEAR ARQUIVOS

for diretory, subfolder, folder in os.walk(main_folder_path):
    for files in folder:
        counter_cdr = 1
        counter_jpeg = 1
        # old_name = os.path.join(os.path.realpath(diretory), files)
        # files = os.path.basename(old_name)
        main_folder_35 = os.path.basename(main_folder_path)[:35]
        
        if files.endswith('.cdr'):

            new = f"'É NOTÍCIA - {main_folder_35}({str(counter_cdr)}).cdr"
            counter_cdr += 1
            os.rename(files, new)
             
        elif files.endswith('.jpeg'):
            new = f"É NOTÍCIA - {main_folder_35}({str(counter_jpeg)}).jpeg"
            counter_jpeg += 1
            os.rename(files, new) 
            
                




# MENSAGEM FINAL
print('Tarefas concluídas com successo!')
