import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from programmas_iestatījumi import iestatījumi, fons

vērtības = {"amplitūde": None, "Lambda": None, "laiks": None, "x": None}

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
                               command=lambda: saglabā_un_zīmē(amplitūds_ievades, lambda_ievades, 
                                                                laika_ievades, x_ievades))
    vērtību_ievade.grid(row=4, column=0, columnspan=2, pady=10)

    logs.rowconfigure(0, weight=1)
    logs.rowconfigure(1, weight=1)
    logs.rowconfigure(2, weight=1)
    logs.rowconfigure(3, weight=1)
    logs.rowconfigure(4, weight=1)

def saglabā_un_zīmē(amplitūds_ievades, lambda_ievades, laika_ievades, x_ievades):
    """Saglabā vērtības un uzzīmē grafiku."""
    try:
        vērtības["amplitūde"] = float(amplitūds_ievades.get())
        vērtības["Lambda"] = float(lambda_ievades.get())
        vērtības["laiks"] = float(laika_ievades.get())
        vērtības["x"] = int(x_ievades.get())

        if vērtības["Lambda"] == 0:
            raise ZeroDivisionError("Lambda nevar būt nulle!")

        zīmēt_grafiku(vērtības)

    except ValueError:
        print("Kļūda: Lūdzu ievadiet tikai skaitļus!")
    except ZeroDivisionError as e:
        print(f"Kļūda: {e}")

def iegūt_vērtības():
    return vērtības

def zīmēt_grafiku(vērtības):
    """Uzzīmē sinusoīdo viļņu grafiku, izmantojot saglabātās vērtības."""
    amplitūde = vērtības["amplitūde"]
    Lambda = vērtības["Lambda"]
    laiks = vērtības["laiks"]
    x_v = vērtības["x"]

    k = 2 * np.pi / Lambda  # Viļņu skaits
    omega = 2 * np.pi  # Lenķiskā frekvence

    x = np.linspace(0, 10, x_v)  # X vērtību masīvs
    y = amplitūde * np.sin(k * x - omega * laiks)  # Aprēķina viļņa vērtības

    plt.figure()
    plt.plot(x, y, label="Sinusoīdālais vilnis")
    plt.xlabel("X pozīcija")
    plt.ylabel("Amplitūda")
    plt.title("Viļņa attēlošana")
    plt.legend()
    plt.grid()
    plt.show()