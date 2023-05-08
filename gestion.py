from tkinter  import *
from tkinter import  ttk,messagebox
import sqlite3 
from sqlite3 import Cursors

class Produit:
    def __init__(self, root):
        self.root=root
        self.root.title("gestion de stock")
        self.root.geometry("1920x1080+0+0")
        #Formulaire
        Gestion_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Gestion_Frame.Place(x=50, y=150, width=600, heigth=700)


        Gestion_title = Label( Gestion_Frame, text="gestion de stock", font=("times new roman", 30, "bold"),bg="cyan")
        Gestion_title.Place(x=50, y=50)

        #nom produit
        nom_produit = Label(Gestion_Frame, text="nom produit", font=("times new roman", 20),bg="cyan")
        nom_produit.place(x=50, y=150)

        id_txt =Entry(Gestion_Frame, font=("times new roman", 20),bg="lightgray")
        id_txt.place(x=220, y=150)

        #Prix
        Prix = Label(Gestion_Frame, text="Prix", font=("times new roman", 20),bg="cyan")
        Prix.place(x=50, y=260)

        Prix_txt =  Entry(Gestion_Frame, font=("times new roman", 20),bg="lightgray")
        Prix_txt.place(x=220, y=260)

        #Quantité
        Quantité = Label(Gestion_Frame, text="Quantité", font=("times new roman", 20),bg="cyan")
        Quantité.place(x=50, y=260)

        Quantité_txt =  Entry(Gestion_Frame, font=("times new roman", 20),bg="lightgray")
        Quantité_txt.place(x=220, y=260)

        #Date de derniere entrée en stock
        Date_de_derniere_entrée_en_stock = Label(Gestion_Frame, text="Date de derniere entrée en stock", font=("times new roman", 20),bg="cyan")
        Date_de_derniere_entrée_en_stock.place(x=50, y=260)

        Date_de_derniere_entrée_en_stock_txt =  Entry(Gestion_Frame, font=("times new roman", 20),bg="lightgray")
        Date_de_derniere_entrée_en_stock_txt.place(x=220, y=260)



        #Buton Ajouter
        btn_ajouter = Button(Gestion_Frame, text="Ajouter", font=("times new roman", 15), bd=10,relief=GROOVE, bg="green")
        btn_ajouter.place(x=10, y=600, width=120)


        #Buton Modifier
        btn_modifier = Button(Gestion_Frame, text="Modifier", font=("times new roman", 15), bd=10,relief=GROOVE, bg="yellow")
        btn_modifier.place(x=150, y=600, width=120)

        #Buton Supprimer
        btn_supprimer = Button(Gestion_Frame, text="Supprimer", font=("times new roman", 15), bd=10,relief=GROOVE, bg="red")
        btn_supprimer.place(x=300, y=600, width=120)

        #Buton Réinitialiser
        btn_reinitialiser = Button(Gestion_Frame, text="Réinitialiser", font=("times new roman", 15), bd=10,relief=GROOVE, bg="gray")
        btn_reinitialiser.place(x=450, y=600, width=120)

        #Recherche
        Details_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Details_Frame.place(x=700, y=150, width=1100, height=700)

        Affiche_resutat = Label(Details_Frame, text="Recherche par", font=("times new roman", 30, "bold"),bg="cyan")
        Affiche_resutat.place(x=50, y=50)
        
        rech = ttk.Combobox(Details_Frame,  font=("times new roman", 20),state="readonly")
        rech["values"]=("nom", "Description", "prix unitaire", "quantité en stock", "Seuil d'alert", "Date de derniere entrée", "Date de derniere sortie")
        rech.place(x=350, y=55, width=180, height=40)

        rech_txt =Entry(Details_Frame,  font=("times new roman", 20),bd=5, relief=GROOVE)
        rech_txt.place(x=550, y=55, width=250, height=40)

        btn_rech =Button(Details_Frame, text="Recherche", font=("times new roman", 15),bd=10, bg="gray",relief=GROOVE)
        btn_rech.place(x=810, y=55, width=120, height=40)

        btn_afftou =Button(Details_Frame, text="Affiche Tous", font=("times new roman", 15),bd=10, bg="gray",relief=GROOVE)
        btn_afftou.place(x=940, y=55, width=135, height=40)

        #Affichage
        result_Frame =Frame(Details_Frame, bd=5, relief=GROOVE,  bg="cyan")
        result_Frame.place(x=10, y=110, width=1070, height=570)

        scroll_x = Scrollbar(result_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Frame, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_Frame,columns=( "nom produit", "prix", "quantité", "Date de derniere entrée en stock"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tabl_resul.heading("nom", text="nom")
        self.tabl_resul.heading("Description", text="Description")
        self.tabl_resul.heading("Prix_unitaire", text="prix unitaire")
        self.tabl_resul.heading("quantité_en_stock", text="quantité en stock")
        self.tabl_resul.heading("Seuil_d'alert", text="Seuil d'alert")
        self.tabl_resul.heading("Date_de_derniere_entrée", text="Date de derniere entrée")
        self.tabl_resul.heading("Date_de_derniere_sortie", text="Date de derniere sortie")

        self.tabl_resul["show"]="heading"

        self.tabl_resul.column("nom", width="100")
        self.tabl_resul.column("Description", width="150")
        self.tabl_resul.column("Prix_unitaire", width="150")
        self.tabl_resul.column("quantité_en_stock", width="150")
        self.tabl_resul.column("Seuil_d'alert", width="150")
        self.tabl_resul.column("Date_de_derniere_entrée", width="150")
        self.tabl_resul.column("Date_de_derniere_sortie", width="200")
        

        self.tabl_resul.pack()

        self.tabl_resul.bind("<ButtonRelease-1>")
        


    root=Tk()
    obj = Produit(root)

root.mainloop()