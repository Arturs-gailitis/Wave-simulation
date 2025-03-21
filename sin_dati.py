import tkinter as tk
from programmas_iestatījumi import iestatījumi, fons

def s_dati(root):
    logs = tk.Toplevel(root)

    iestatījumi(logs, 500, 400, 'Ievada mainīgo vērtības priekš sinusoīdo viļņu funkcijas')

    fons(logs, 500, 400)

    logs.columnconfigure(0, weight=1) 
    logs.columnconfigure(1, weight=1)

    tk.Label(logs, text='Amplitūde', background='lightblue').grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Lambda', background='lightblue').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='Laiks', background='lightblue').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(logs, text='X', background='lightblue').grid(row=3, column=0, padx=10, pady=5, sticky="e")

    amplitūds_ievades = tk.Entry(logs, width=10)
    amplitūds_ievades.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    lambda_ievades = tk.Entry(logs, width=10)
    lambda_ievades.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    laika_ievades = tk.Entry(logs, width=10)
    laika_ievades.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    x_ievades = tk.Entry(logs, width=10)
    x_ievades.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    vērtību_ievade = tk.Button(logs, text='Ievada vērtības',
                               command=lambda: saglabā_vērtības(amplitūds_ievades, lambda_ievades, 
                                                                laika_ievades, x_ievades))
    vērtību_ievade.grid(row=4, column=0, columnspan=2, pady=10)

    logs.rowconfigure(0, weight=1)
    logs.rowconfigure(1, weight=1)
    logs.rowconfigure(2, weight=1)
    logs.rowconfigure(3, weight=1)
    logs.rowconfigure(4, weight=1)

def saglabā_vērtības(amplitūds_ievades, lambda_ievades, laika_ievades, x_ievades):
    amplitūde = amplitūds_ievades.get()
    Lambda = lambda_ievades.get()
    laiks = laika_ievades.get()
    x = x_ievades.get()

    return amplitūde, Lambda, laiks, x
 