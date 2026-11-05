import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


headers = {"x-cg-demo-api-key": 'CG-FNsnpoKPiovJfB1vPtXd5eRu'}

Crypto = {
    'Bitcoin': ["bitcoin", "Bitcoin", "btc"],
    'BnB': ["binancecoin", "BNB", "bnb"],
    'Official Trump': ["official-trump", "Official Trump", "trump"],
    'Ethereum': ["ethereum", "Ethereum", "eth"],
    'Shiba Imu': ["shiba-inu", "Shiba Inu", "shib"]
}

# --- fonction API ---
def Info(Choix, Devise):
    '''
    --------------------
    Description:
    Collecte les infos liées a une crypto precise

    Params: Choix de la crypto (str)
            Devise choisie (str)

    Return:
    Dictionnaire contenant toutes les informations de la crypto
    --------------------
    '''
    url = "https://api.coingecko.com/api/v3/coins/markets"
    InfoQuery = {"vs_currency": Devise, "ids": Crypto[Choix][0]}
    response = requests.get(url, headers=headers, params=InfoQuery)
    return response.json()

def fetch_range(Choix, seconds, devise):
    '''
    --------------------
    Description:
    Collecte les prix d'une crypto dans un temps donne

    Params: Choix de la crypto (str)
            Devise choisie (str)
            Temps en seconde (int)

    Return:
    Dictionnaire contenant tous les prix associé a une crypto dans un lapse de temps precis
    --------------------
    '''
    current_time = int(time.time())
    before = current_time - seconds
    url = f"https://api.coingecko.com/api/v3/coins/{Choix.lower()}/market_chart/range"
    InfoQuery = {"vs_currency": devise, "from": before, "to": current_time}
    response = requests.get(url, headers=headers, params=InfoQuery)
    return response.json()

#Cree le graph
def Graph(data):
    '''
    --------------------
    Description:
    Cree un graph avec les prix d'une crypto dans un temps donne

    Params: Dictionnaire contenant tous les prix associé a une crypto dans un lapse de temps precis (dict)

    Return:
    Graph avec les prix d'une crypto dans un temps donne
    --------------------
    '''
    data = data['prices']
    dates = [datetime.datetime.fromtimestamp(p[0]/1000) for p in data]
    prix = [p[1] for p in data]

    fig, ax = plt.subplots(figsize=(5,3))
    for i in range(1, len(prix)):
        color = 'green' if prix[i] >= prix[i-1] else 'red'
        ax.plot(dates[i-1:i+1], prix[i-1:i+1], color=color)

    fig.patch.set_facecolor("green")
    ax.set_ylabel("Prix", color='black')
    ax.set_facecolor("black")
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')

    fig.tight_layout()
    fig.autofmt_xdate(rotation=30)


    #Supprime ancien graph
    for widget in graph_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)

    canvas.draw()
    canvas.get_tk_widget().pack()


# --- Action boutons ---
    '''
    DOCSTRING ASSOCIE AUX FONCTIONS 'ouvrir_fenetre{temps}'
    --------------------
    Description:
    Affiche le graph

    Params: 

    Return:
    Graph
    --------------------
    '''
def ouvrir_fenetrean():
    afficher_graph( 31536000)

def ouvrir_fenetresixmois():
    afficher_graph( 15552000)

def ouvrir_fenetremois():
    afficher_graph( 2592000)

def ouvrir_fenetresemaine():
    afficher_graph( 604800)

def ouvrir_fenetrejour():
    afficher_graph( 86400)

def ouvrir_fenetreheure():
    afficher_graph( 3600)

def afficher_graph( seconds):
    '''
    --------------------
    Description:
    Affiche le graph

    Params: Nombre de secondes (int)

    Return:
    Graph avec les prix d'une crypto dans un temps donne
    --------------------
    '''
    choix = titre_variable1.get()
    devise = titre_variable.get()

    if choix not in Crypto or devise == "Choisissez une devise":
        return

    # Update prix
    info = Info(choix, devise)
    if info:
        prix_actuel = info[0]['market_cap']
        formatted = f"{int(prix_actuel):,}"
        price_label.config(text=f"Valeur Capitalisation Boursiere de {choix} : {formatted} {devise}")

    # Montre graph
    data = fetch_range(Crypto[choix][0], seconds, devise)
    Graph(data)

def update_image(*args):
    '''
    --------------------
    Description:
    Change l'image

    Params: 

    Return:
    L'image modifie par rapport a la crypto choisie
    --------------------
    '''
    choix = titre_variable1.get()
    #Enleve la vielle photo
    for widget in image_label.winfo_children():
        widget.destroy()

    try:
        if choix == "Ethereum":
            image_pil = Image.open('./Images/ETH.png').resize((100, 100))
        elif choix == "Bitcoin":
            image_pil = Image.open('./Images/Bitcoin.png').resize((100, 100))
        elif choix == "Official Trump":
            image_pil = Image.open('./Images/Trump.png').resize((100, 100))
        elif choix == "Shiba Imu":
            image_pil = Image.open('./Images/Shiba.png').resize((100, 100))
        elif choix == "BnB":
            image_pil = Image.open('./Images/BNB.png').resize((100, 100))
        
        else:
            image_pil = Image.open('cryptorespect.png').resize((50, 50))

        img = ImageTk.PhotoImage(image_pil)
        image_label.config(image=img)
        image_label.image = img
    except :
        print("Erreur chargement image")

# --- Fenetre principale ---
fenetre = tk.Tk()
fenetre.title("Cryptorespect")
fenetre.geometry("900x600")
fenetre.configure(bg='black')

titre_variable1 = tk.StringVar(value="Choisissez une crypto")
titre_variable = tk.StringVar(value="Choisissez une devise")

# Menus
menucrypto = tk.OptionMenu(fenetre, titre_variable1, *Crypto.keys())
menucrypto.config(bg="GREEN", activebackground="GREEN", activeforeground="BLACK")
menucrypto["menu"].config(bg="GREEN", activebackground="GREEN", activeforeground="BLACK")
menucrypto.pack(side="left")

menumonnaie = tk.OptionMenu(fenetre, titre_variable, "USD", "EUR", "GBP", "INR", "KRW", "JPY", "MXN")
menumonnaie.config(bg="GREEN", activebackground="GREEN", activeforeground="BLACK")
menumonnaie["menu"].config(bg="GREEN", activebackground="GREEN", activeforeground="BLACK")
menumonnaie.pack(side="right")

lbl = Label(fenetre, text="Cryptorespect", bg="#20C20E")
lbl.pack()

# Valuer capitalisation boursiere
price_label = Label(fenetre, text="Sélectionnez une crypto et une devise", font=("Arial", 14), bg="black", fg="green")
price_label.pack(pady=10)


image_label = tk.Label(fenetre, bg="black")
image_label.pack(pady=10)



# Changement d'image en continu
titre_variable1.trace_add("write", update_image)

# Graph frame
graph_frame = Frame(fenetre, bg="black")
graph_frame.pack(fill="both", expand=True)

# Boutons
Button(fenetre, text="1 an", bg="green", command=ouvrir_fenetrean).pack(side="right", padx=10, expand= True, fill='both', pady=20)
Button(fenetre, text="6 mois", bg="green", command=ouvrir_fenetresixmois).pack(side="right", padx=10, expand= True, fill='both', pady=20)
Button(fenetre, text="1 mois", bg="green", command=ouvrir_fenetremois).pack(side="right", padx=10, expand= True, fill='both', pady=20)
Button(fenetre, text="1 semaine", bg="green", command=ouvrir_fenetresemaine).pack(side="right", padx=10, expand= True, fill='both', pady=20)
Button(fenetre, text="1 jour", bg="green", command=ouvrir_fenetrejour).pack(side="right", padx=10, expand= True, fill='both', pady=20)
Button(fenetre, text="1 heure", bg="green", command=ouvrir_fenetreheure).pack(side="right", padx=10, expand= True, fill='both', pady=20)

fenetre.mainloop()
