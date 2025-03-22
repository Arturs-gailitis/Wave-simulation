import tkinter as tk
import os

from PIL import Image, ImageTk

def iestatījumi(root, x_ass, y_ass, lapas_tituls):

    izmērs = str(x_ass) + 'x' + str(y_ass)

    root.geometry(izmērs) # Pielāgo loga izmēru

    root.title(lapas_tituls) # Iedod logam nosaukumu

    root.config()

# Punkcija ar kuru izslēdz programmu
def programmas_beigas(root):

    root.destroy()

def fons(root, x, y, bilde):
    
    ceļš = os.path.join("bildes", bilde) # Parāda fona bildes atrašanos

    fona_bilde = Image.open(ceļš) # Bilde tiek atvērta 
    fona_bilde = fona_bilde.resize((x, y)) # Maina bildes izmērus
    fons = ImageTk.PhotoImage(fona_bilde) #Pārveido attēlu lai to varētu ielikt kā fonu

    fona_label = tk.Label(root, image=fons) # Tiek izveidots Label elements, kurā atrodās attēls
    fona_label.place(relwidth=1, relheight=1) #Ieliek bildi pa visu lauku
    fona_label.image = fons # Saglabā elementu