from tkinter import PhotoImage
import pygame
import customtkinter as ctk
from customtkinter import *

pygame.mixer.init()


def iniciar_musica():
    escolher_musica = filedialog.askopenfilename(
        title = "Escolha um arquivo",
        filetypes = (("Music Files","*.mp3"),))
    
    pygame.mixer.music.load(escolher_musica)

    pygame.mixer.music.play()


def pausar_musica():
    pygame.mixer.music.pause()

def resumir_musica():
    pygame.mixer.music.unpause()

def parar_musica():
    pygame.mixer.fadeout(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()


def volume_geral(value):
    volume_numero = value
    print(volume_numero)
    pygame.mixer.music.set_volume(volume_numero)


# def volume_acima():
#     pygame.mixer.Sound.set_volume()


window = ctk.CTk()
window.title("MP3 Player")
window.geometry("370x150")

# Definindo os icones
# pasta_icones = '/home/kjunda01/PROJETOS/Curso em Video Python/Player de Musica/icons/'
# icone_pausa = PhotoImage(file= "https://cdn-icons-png.flaticon.com/512/5644/5644535.png")
# icone_iniciar = PhotoImage(file= pasta_icones + "play-button.png")
# icone_parar = PhotoImage(file= pasta_icones + "stop-button.png")
# icone_resumir = PhotoImage(file= pasta_icones + "play-and-pause-button.png")


# criação dos botoes
botao_pausa = ctk.CTkButton(window,
                            text="Pausar",
                            command=pausar_musica
                            )

botao_iniciar = ctk.CTkButton(window,
                              text="Selecionar Musica",
                              command=iniciar_musica
                              )

botao_parar = ctk.CTkButton(window,
                            text="Parar",
                            command=parar_musica
                            )

botao_resumir = ctk.CTkButton(window,
                              text="Resumir",
                              command=resumir_musica
                              )

volume_bar = ctk.CTkSlider(master=window,
                           command=volume_geral,
                           )

#botoes na tela
# botao_iniciar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
botao_iniciar.grid(row=0, column=0, padx=1, pady=10)
botao_parar.grid(row=0, column=1, padx=1, pady=10)
botao_pausa.grid(row=1, column=0, padx=1, pady=10)
botao_resumir.grid(row=1, column=1, padx=1, pady=10)
volume_bar.grid(row=1, column=2, padx=1, pady=10,)



window.mainloop()
