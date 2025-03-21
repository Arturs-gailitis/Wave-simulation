import tkinter as tk
import os

from PIL import Image, ImageTk
from programmas_iestatījumi import iestatījumi, programmas_beigas

root = tk.Tk()

iestatījumi(root, 500, 400)

ceļš = os.path.join("bildes", "fona_attēls.jpg")
fona_bilde = Image.open(ceļš) 
fona_bilde = fona_bilde.resize((500, 400))
fons = ImageTk.PhotoImage(fona_bilde)

fona_label = tk.Label(root, image=fons)
fona_label.place(relwidth=1, relheight=1)

par_pogām_tekts = tk.Label(root, text='Izvēlaties ar kādu funkciju attēlosiet viļņus', font=('Ariel', 14), background='lightblue')
par_pogām_tekts.pack(pady=10)

sīnusa_poga = tk.Button(root, text='Sinusoīdo viļņu funkcija', background='lightblue')
sīnusa_poga.pack(pady=10)

kosīnusa_poga = tk.Button(root, text='Kosinusoidālā viļņa funkcija', background='lightblue')
kosīnusa_poga.pack(pady=10)

beigu_poga = tk.Button(root, text='Programmas beigas', command=lambda: programmas_beigas(root), background='lightblue')
beigu_poga.pack(pady=10)

root.mainloop()