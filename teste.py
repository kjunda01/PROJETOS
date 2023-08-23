import os 

main_folder_path = os.getcwd()

dest = main_folder_path.rfind(f'{os.path.basename(main_folder_path)}')

barra = main_folder_path.rfind(f'{os.path.basename(main_folder_path)}')-1

main = main_folder_path[barra:]
print(os.walk(main_folder_path))


print(dest)
print(barra)
print(main[:30])