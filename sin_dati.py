import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from programmas_iestatījumi import iestatījumi, fons

def s_dati(root):
    
    logs = tk.Toplevel(root) # Tiek atvērta jauns apakšlogs

    iestatījumi(logs, 500, 400, 'Ievada mainīgo vērtības priekš sinusoīdo viļņu funkcijas')

    fons(logs, 500, 400)

    # Tiek izveidotas kolonnas un rindas, kuros tiks ielikti elementi, lai tie izskatītos kārtīgi
    logs.columnconfigure(0, weight=1) 
    logs.columnconfigure(1, weight=1)

    logs.rowconfigure(0, weight=1)
    logs.rowconfigure(1, weight=1)
    logs.rowconfigure(2, weight=1)
    logs.rowconfigure(3, weight=1)
    logs.rowconfigure(4, weight=1)

    #T iek izveidoti Label, kas paskaidro kādas vērtības ir domātas noteiktajiem texta logiem 
    tk.Label(logs, text='Amplitūde', background='lightblue').grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Lambda', background='lightblue').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Laiks', background='lightblue').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='X', background='lightblue').grid(row=3, column=0, padx=10, pady=5, sticky="e")

    # Lietotājs raksta iekšā teksta logos vērtības
    amplitūds_ievades = tk.Entry(logs, width=10)
    amplitūds_ievades.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    lambda_ievades = tk.Entry(logs, width=10)
    lambda_ievades.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    laika_ievades = tk.Entry(logs, width=10)
    laika_ievades.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    x_ievades = tk.Entry(logs, width=10)
    x_ievades.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    #Tiek radīta poga, kas apkopos uz aizsūtīs vērtības uz grafikas zīmēšanu
    vērtību_ievade = tk.Button(logs, text='Ievada vērtības',
                               command=lambda: saglabā_un_zīmē(amplitūds_ievades, lambda_ievades, 
                                                                laika_ievades, x_ievades))
    vērtību_ievade.grid(row=4, column=0, columnspan=2, pady=10)

def saglabā_un_zīmē(amplitūds_ievades, lambda_ievades, laika_ievades, x_ievades):
    
    #Nepieciešamās vērtības
    amplitūde = float(amplitūds_ievades.get()) # Amplitūde
    Lambda = float(lambda_ievades.get()) # Viļņa garums
    laiks = float(laika_ievades.get()) # Laiks
    x_v = int(x_ievades.get()) # x vērtības

    k = 2 * np.pi / Lambda  # Viļņu skaits
    omega = 2 * np.pi  # Lenķiskā frekvence

    x = np.linspace(0, 10, x_v)  # X vērtību masīvs
    y = amplitūde * np.sin(k * x - omega * laiks)  # Aprēķina viļņa vērtības

    #Uzzīmē grafiku
    plt.figure()

    plt.plot(x, y)

    plt.xlabel("X pozīcija")
    plt.ylabel("Amplitūda")

    plt.title("Vilnis kurš ir veidots ar sinusoīdo viļņu funkciju")

    plt.legend()

    plt.grid()

    plt.show()