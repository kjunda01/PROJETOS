import os
import pathlib
directory = os.getcwd()
print(pathlib.Path(directory))

image_name = 'É notícia - '

i = 0
for file in os.listdir(directory):
    new_file_name = image_name + directory.strip(directory)[-1] + str(i) + ".jpg" #here you can change the extention of your renmamed file.
    os.rename(file,new_file_name)
    i += 1

input("Renamed all Images!!")