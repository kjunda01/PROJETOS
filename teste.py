import flet as ft
from flet import IconButton, Page, Row, TextField, icons, Text

def main(page= ft.Page):
    page.title = "Mp3 Music Player"
    page.vertical_alignment = "center"
    page.update()

    escolher_musica = Text()
    
ft.app(target=main, view=ft.AppView.FLET_APP)