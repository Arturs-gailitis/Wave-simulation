import tkinter as tk
import os

from PIL import Image, ImageTk

def iestatījumi(root, x_ass, y_ass, lapas_tituls):

    izmērs = str(x_ass) + 'x' + str(y_ass)

    root.geometry(izmērs)

    root.title(lapas_tituls)

    root.config()

def programmas_beigas(root):

    root.destroy()

def fons(root, x, y):
    
    ceļš = os.path.join("bildes", "fona_attēls.jpg")

    fona_bilde = Image.open(ceļš)
    fona_bilde = fona_bilde.resize((x, y))
    fons = ImageTk.PhotoImage(fona_bilde)

    fona_label = tk.Label(root, image=fons)
    fona_label.place(relwidth=1, relheight=1)
    fona_label.image = fons