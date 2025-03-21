import tkinter as tk 

from programmas_iestatījumi import iestatījumi, programmas_beigas, fons
from sin_dati import s_dati

#Izveido galveno grafisko logu
root = tk.Tk()

#Iestada galvenos x, y izmērus un arī pievieno loga nosaukumu
iestatījumi(root, 500, 400, 'Programmas par viļņu zīmēšanu galvenā izvelne')

#eiestada fona bildi
fons(root, 500, 400)

#Label, kas lietotājam liek saprast par programmu
par_pogām_tekts = tk.Label(root, text='Izvēlaties ar kādu funkciju attēlosiet viļņus', font=('Ariel', 14), background='lightblue')
par_pogām_tekts.pack(pady=10)

#Poga uz sinusoīdo viļņu funkcijas izveidošanu
sīnusa_poga = tk.Button(root, text='Sinusoīdo viļņu funkcija', background='lightblue',command=lambda: s_dati(root))
sīnusa_poga.pack(pady=10)

#Poga uz kosinusoidālā viļņu funkcijas izveidošanu
kosīnusa_poga = tk.Button(root, text='Kosinusoidālā viļņa funkcija', background='lightblue')
kosīnusa_poga.pack(pady=10)

#Poga ar kuru var izslēgt programmu
beigu_poga = tk.Button(root, text='Programmas beigas', command=lambda: programmas_beigas(root), background='lightblue')
beigu_poga.pack(pady=10)

root.mainloop()