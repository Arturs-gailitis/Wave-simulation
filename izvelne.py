import tkinter as tk

from programmas_iestatījumi import iestatījumi, programmas_beigas, fons
from sin_dati import s_dati

root = tk.Tk()

iestatījumi(root, 500, 400, 'Programmas par viļņu zīmēšanu galvenā izvelne')

fons(root, 500, 400)

par_pogām_tekts = tk.Label(root, text='Izvēlaties ar kādu funkciju attēlosiet viļņus', font=('Ariel', 14), background='lightblue')
par_pogām_tekts.pack(pady=10)

sīnusa_poga = tk.Button(root, text='Sinusoīdo viļņu funkcija', background='lightblue',command=lambda: s_dati(root))
sīnusa_poga.pack(pady=10)

kosīnusa_poga = tk.Button(root, text='Kosinusoidālā viļņa funkcija', background='lightblue')
kosīnusa_poga.pack(pady=10)

beigu_poga = tk.Button(root, text='Programmas beigas', command=lambda: programmas_beigas(root), background='lightblue')
beigu_poga.pack(pady=10)

root.mainloop()