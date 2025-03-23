import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from programmas_iestatījumi import iestatījumi, fons, programmas_beigas

def g_dati(root):
    
    logs = tk.Toplevel(root) # Tiek atvērta jauns apakšlogs

    iestatījumi(logs, 500, 400, 'Ievada mainīgo vērtības priekš Gaussa viļņu funkcijas')

    fons(logs, 500, 400, "fona_attēls1.jpeg")

    # Tiek izveidotas kolonnas un rindas, kuros tiks ielikti elementi, lai tie izskatītos kārtīgi
    logs.columnconfigure(0, weight=1) 
    logs.columnconfigure(1, weight=1)

    logs.rowconfigure(0, weight=1)
    logs.rowconfigure(1, weight=1)
    logs.rowconfigure(2, weight=1)
    logs.rowconfigure(3, weight=1)
    logs.rowconfigure(4, weight=1)
    logs.rowconfigure(5, weight=1)
    logs.rowconfigure(6, weight=1)

    #T iek izveidoti Label, kas paskaidro kādas vērtības ir domātas noteiktajiem texta logiem 
    tk.Label(logs, text='Amplitūde', background='darkgrey').grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Viļņa garums', background='darkgrey').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Centra pozīcija', background='darkgrey').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Platuma vērtība', background='darkgrey').grid(row=3, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Cik daudz cipari būs priekš X Pozīcijas', 
             background='darkgrey').grid(row=4, column=0, padx=10, pady=5, sticky="e")

    # Lietotājs raksta iekšā teksta logos vērtības
    amplitūds_ievades = tk.Entry(logs, width=10)
    amplitūds_ievades.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    lambda_ievades = tk.Entry(logs, width=10)
    lambda_ievades.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    centra_ievades = tk.Entry(logs, width=10)
    centra_ievades.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    platuma_ievades = tk.Entry(logs, width=10)
    platuma_ievades.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    x_ievades = tk.Entry(logs, width=10)
    x_ievades.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    #Tiek radīta poga, kas apkopos uz aizsūtīs vērtības uz grafikas zīmēšanu
    vērtību_ievade = tk.Button(logs, text='Ievada vērtības',
                               command=lambda: saglabā_un_zīmē_g(amplitūds_ievades, lambda_ievades, 
                                                                centra_ievades, platuma_ievades, 
                                                                x_ievades), background='darkgrey')
    vērtību_ievade.grid(row=5, column=0, columnspan=2, pady=10)

    apakšlapas_iziešana = tk.Button(logs, text='Iziet ārā uz galveno sadaļu', 
                                    command= lambda: programmas_beigas(logs), background='darkgray')
    apakšlapas_iziešana.grid(row=6, column=0, columnspan=2, pady=10)

def saglabā_un_zīmē_g(amplitūds_ievades, lambda_ievades, centra_ievades, platuma_ievades, x_ievades):
    
    #Nepieciešamās vērtības
    amplitūde = float(amplitūds_ievades.get()) # Amplitūde
    Lambda = float(lambda_ievades.get()) # Viļņa garums
    xo = float(centra_ievades.get()) # Centra pozīcija
    sigma = float(platuma_ievades.get()) # Platums, kas nosaka viļņu izkliedi
    x_v = int(x_ievades.get()) # Cik daudz ciparu pozīcijā X būs starp intervāliem 0 un 10 

    k = 2 * np.pi / Lambda  # Viļņu skaits

    x = np.linspace(0, 10, x_v)  # Pozīciju masīvs
    y = amplitūde * np.exp(-((x - xo) ** 2) / (2 * sigma ** 2)) * np.sin(k * x)  # Aprēķina Gaussa viļņa vērtības

    #Uzzīmē grafiku
    plt.figure()

    plt.plot(x, y)

    plt.xlabel("X pozīcija")
    plt.ylabel("Amplitūda")

    plt.title("Vilnis kurš ir veidots ar Gaussa viļņu funkciju")

    plt.grid()

    plt.show()