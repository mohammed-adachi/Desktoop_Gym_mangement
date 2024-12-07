import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class MembreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Membres")
        self.root.geometry("600x400")

        # Frame principal
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(expand=True, fill='both')

        # Frame des boutons principaux
        self.creer_menu_principal()

    def creer_menu_principal(self):
        # Nettoyer le frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Boutons principaux
        btn_liste_membres = ttk.Button(
            self.main_frame, 
            text="Lister les Membres", 
            style='primary.TButton',
            command=self.afficher_liste_membres
        )
        btn_liste_membres.pack(pady=10, fill='x')

        btn_inscription = ttk.Button(
            self.main_frame, 
            text="Inscription", 
            style='success.TButton',
            command=self.afficher_inscription
        )
        btn_inscription.pack(pady=10, fill='x')

        btn_paiement = ttk.Button(
            self.main_frame, 
            text="Paiement", 
            style='warning.TButton',
            command=self.afficher_paiement
        )
        btn_paiement.pack(pady=10, fill='x')

    def afficher_liste_membres(self):
        
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Titre
        ttk.Label(self.main_frame, text="Liste des Membres", style='primary.TLabel', font=('Arial', 16)).pack(pady=10)

        # Tableau des membres
        colonnes = ('Nom', 'Prénom', 'Email')
        table = ttk.Treeview(self.main_frame, columns=colonnes, show='headings')
        
        for col in colonnes:
            table.heading(col, text=col)
        
        # Exemple de données
        membres = [
            ('Dupont', 'Jean', 'jean.dupont@email.com'),
            ('Martin', 'Marie', 'marie.martin@email.com')
        ]
        
        for membre in membres:
            table.insert('', 'end', values=membre)
        
        table.pack(expand=True, fill='both', padx=10, pady=10)

        # Bouton Retour
        btn_retour = ttk.Button(
            self.main_frame, 
            text="Retour", 
            style='secondary.TButton',
            command=self.creer_menu_principal
        )
        btn_retour.pack(pady=10, fill='x')
        btn_liste_membress = ttk.Button(
            self.main_frame, 
            text="Lister les Membres", 
            style='primary.TButton',
            command=self.afficher_liste_membres
        )
        
        btn_liste_membress.pack(pady=10, fill='x')
        btn_inscription = ttk.Button(
            self.main_frame, 
            text="Inscription", 
            style='success.TButton',
            command=self.afficher_inscription
        )
        btn_inscription.pack(pady=10, fill='x')
        btn_paiement = ttk.Button(
            self.main_frame, 
            text="Paiement", 
            style='warning.TButton',
            command=self.afficher_paiement
        )
        btn_paiement.pack(pady=10, fill='x')

    def afficher_inscription(self):
        # Nettoyer le frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Titre
        ttk.Label(self.main_frame, text="Inscription", style='success.TLabel', font=('Arial', 16)).pack(pady=10)

        # Formulaire d'inscription
        ttk.Label(self.main_frame, text="Nom:").pack()
        nom_entry = ttk.Entry(self.main_frame)
        nom_entry.pack()

        ttk.Label(self.main_frame, text="Prénom:").pack()
        prenom_entry = ttk.Entry(self.main_frame)
        prenom_entry.pack()

        ttk.Label(self.main_frame, text="Email:").pack()
        email_entry = ttk.Entry(self.main_frame)
        email_entry.pack()

        btn_valider = ttk.Button(
            self.main_frame, 
            text="Valider", 
            style='success.TButton'
        )
        btn_valider.pack(pady=10)

        # Bouton Retour
        btn_retour = ttk.Button(
            self.main_frame, 
            text="Retour", 
            style='secondary.TButton',
            command=self.creer_menu_principal
        )
        btn_retour.pack(pady=10, fill='x')
        btn_retour.pack(pady=10, fill='x')
        btn_liste_membress = ttk.Button(
            self.main_frame, 
            text="Lister les Membres", 
            style='primary.TButton',
            command=self.afficher_liste_membres
        )
        
        btn_liste_membress.pack(pady=10, fill='x')
        btn_inscription = ttk.Button(
            self.main_frame, 
            text="Inscription", 
            style='success.TButton',
            command=self.afficher_inscription
        )
        btn_inscription.pack(pady=10, fill='x')
        btn_paiement = ttk.Button(
            self.main_frame, 
            text="Paiement", 
            style='warning.TButton',
            command=self.afficher_paiement
        )
        btn_paiement.pack(pady=10, fill='x')
    def afficher_paiement(self):
        # Nettoyer le frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Titre
        ttk.Label(self.main_frame, text="Paiement", style='warning.TLabel', font=('Arial', 16)).pack(pady=10)

        # Options de paiement
        ttk.Label(self.main_frame, text="Montant:").pack()
        montant_entry = ttk.Entry(self.main_frame)
        montant_entry.pack()

        ttk.Label(self.main_frame, text="Mode de Paiement:").pack()
        modes_paiement = ['Carte Bancaire', 'PayPal', 'Virement']
        mode_var = tk.StringVar()
        mode_combobox = ttk.Combobox(self.main_frame, textvariable=mode_var, values=modes_paiement)
        mode_combobox.pack()

        btn_payer = ttk.Button(
            self.main_frame, 
            text="Confirmer Paiement", 
            style='warning.TButton'
        )
        btn_payer.pack(pady=10)

        # Bouton Retour
        btn_retour = ttk.Button(
            self.main_frame, 
            text="Retour", 
            style='secondary.TButton',
            command=self.creer_menu_principal
        )
        btn_retour.pack(pady=10, fill='x')
        btn_retour.pack(pady=10, fill='x')
        btn_liste_membress = ttk.Button(
            self.main_frame, 
            text="Lister les Membres", 
            style='primary.TButton',
            command=self.afficher_liste_membres
        )
        
        btn_liste_membress.pack(pady=10, fill='x')
        btn_inscription = ttk.Button(
            self.main_frame, 
            text="Inscription", 
            style='success.TButton',
            command=self.afficher_inscription
        )
        btn_inscription.pack(pady=10, fill='x')
        btn_paiement = ttk.Button(
            self.main_frame, 
            text="Paiement", 
            style='warning.TButton',
            command=self.afficher_paiement
        )
        btn_paiement.pack(pady=10, fill='x')
def main():
    root = ttk.Window(themename="flatly")
    app = MembreApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()