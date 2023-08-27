import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

root = tk.Tk()
URL = "https://cdn-icons-png.flaticon.com/512/27/27223.png"
u = urllib.request.urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im = im.resize((256,256),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(im)

button = tk.Button(image=photo,width=256,height=256,compound="c")
button.image = photo
button.pack()

root.mainloop()