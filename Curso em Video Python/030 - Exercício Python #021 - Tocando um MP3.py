from tkinter import PhotoImage, filedialog
import pygame
from pygame import *
import customtkinter as ctk

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
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def volume_geral(value):
    pygame.mixer.music.set_volume(value)

def duracao():
    pygame.mixer.music.get_pos()

# Propriedades da janela principal
window = ctk.CTk()
window.title("MP3 Player")
window.geometry("800x600")


# criação dos botoes
botao_pausa = ctk.CTkButton(window,
                            text="Pausar",
                            command=pausar_musica,
                            corner_radius=45,
                            )

botao_selecionar = ctk.CTkButton(window,
                              text="Selecionar\nMusica",
                              command=iniciar_musica,
                              corner_radius=45,
                              )

botao_parar = ctk.CTkButton(window,
                            text="Parar",
                            command=parar_musica,
                            corner_radius=45,
                            )

botao_resumir = ctk.CTkButton(window,
                              text="Resumir",
                              command=resumir_musica,
                              corner_radius=45,
                              )

volume_bar = ctk.CTkSlider(master=window,
                           command=volume_geral,
                           orientation='vertical',
                           height=600,
                           )



#botoes na tela - place
# botao_selecionar.place(relx=0.09, rely=0.01, anchor=ctk.N)
# botao_parar.place(relx=0.09, rely=0.9, anchor=ctk.N)
# botao_pausa.place(relx=0.09, rely=0.9, anchor=ctk.N)
# botao_resumir.place(relx=0.09, rely=0.9, anchor=ctk.N)
# volume_bar.place(relx=0.97, rely=0.5, anchor=ctk.CENTER)


#botoes na tela - grid
botao_selecionar.grid(row=0, column=0, padx=1, pady=10)
botao_parar.grid(row=0, column=1, padx=1, pady=10)
botao_pausa.grid(row=1, column=0, padx=1, pady=10)
botao_resumir.grid(row=1, column=1, padx=1, pady=10)
volume_bar.grid(row=1, column=2, padx=1, pady=10,)



window.mainloop()
