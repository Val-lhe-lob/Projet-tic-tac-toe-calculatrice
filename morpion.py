import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import webbrowser



class TicTacToe:
    #Initialisation des instances de la Class ( 0 dans la plupart des instances )
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.geometry("500x500")
        self.tour = 0
        self.score_joueur1 = 0
        self.score_joueur2 = 0
        self.score_robot = 0
        self.boutons = [[None for j in range(3)] for i in range(3)] # Initialisation de la grille de boutons
        self.adversaire = ""
        self.label_tour = tk.Label(self.fenetre, text="Tour du joueur : Joueur 1", font=('Helvetica', 12, 'bold'))
        self.label_score = tk.Label(self.fenetre, text="Score : Joueur 1 - 0 | Joueur 2 - 0 | Robot - 0", font=('Helvetica', 12, 'bold'))

    #Méthodes réinitialisation du jeu ( création du mappage de la grille de boutons , et remplacement du texte de la grille par un texte vide)
    def reinitialiser_jeu(self):
        for i in range(3):#Remplaçage du texte de la grille par un string vide, on parcourt chaque bouton de la grille et le remplace grâce aux indices des boutons
            for j in range(3):
                self.boutons[i][j].config(text="")
        #Choix de l'adversaire et initialisation des tours à 0
        choix_adversaire = messagebox.askquestion("Choix de l'adversaire", "Voulez-vous jouer contre un robot ?", icon='question')
        self.adversaire = "robot" if choix_adversaire == "yes" else "humain"
        self.tour = 0
        self.label_tour.config(text="Tour du joueur : Joueur 1")

    #On appelle la méthode avec en paramètre les indices du bouton où remplacer le texte
    def bouton_clic(self, i, j):
        #Vérification si le texte du bouton est vide
        if self.boutons[i][j]["text"] == "":
            #Vérification du tour, et en fonction , X ou O
            if self.tour % 2 == 0:
                self.boutons[i][j].config(text="X")
                joueur = "Joueur 2"
            else:
                self.boutons[i][j].config(text="O")
                joueur = "Joueur 1" if self.adversaire == "robot" else "Joueur 1"
            #Indentation du tour
            self.tour += 1
            #Vérification de la victoire / match nul 
            if self.verifier_victoire():
                messagebox.showinfo("Fin de partie", f"Le joueur {joueur} a gagné !")
                self.mettre_a_jour_score(joueur)
                self.afficher_rejouer(joueur)
            elif self.verifier_match_nul():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.afficher_rejouer(joueur)
            elif self.tour % 2 == 1 and self.adversaire == "robot":
                self.label_tour.config(text="Tour du joueur : Robot réfléchit...")
                self.fenetre.update()
                time.sleep(0.5)
                self.jouer_robot()

            self.label_tour.config(text=f"Tour du joueur : {joueur}")
        #Si la case est déjà utilisé, on avertit le joueur et le tour n'est pas indenté
        else:
            messagebox.showerror("Case occupée", "Cette case est déjà occupée. Choisissez une autre case.")

    #Méthode pour vérifier la victoire qui retourne true si la victoire est vérifié
    def verifier_victoire(self):
        for i in range(3):
            #Vérification horizontale
            if self.boutons[i][0]["text"] == self.boutons[i][1]["text"] == self.boutons[i][2]["text"] != "":
                return True
        #Vérification verticale
        for j in range(3):
            if self.boutons[0][j]["text"] == self.boutons[1][j]["text"] == self.boutons[2][j]["text"] != "":
                return True
        #Vérification diagonale
        if self.boutons[0][0]["text"] == self.boutons[1][1]["text"] == self.boutons[2][2]["text"] != "":
            return True
        if self.boutons[0][2]["text"] == self.boutons[1][1]["text"] == self.boutons[2][0]["text"] != "":
            return True
        #Si lors de l'appel de la méthode , on ne rentre dans aucun des critères, return false, aucun des joueurs n'a encore gagné
        return False
    

    #méthode de vérification du match nul
    def verifier_match_nul(self):
        #Vérification if
        for i in range(3):
            for j in range(3):
                #si au moins un texte des boutons est un string vide
                if self.boutons[i][j]["text"] == "":
                    #on retourne faux, le match n'est pas nul et donc la partie continue
                    return False
        #Sinon return true, la partie se termine en match nul
        return True
    #Méthode pour fermer la fenetre
    def quitter_jeu(self):
        self.fenetre.quit()

    #Méthode pour afficher une demande pour rejouer
    def afficher_rejouer(self, joueur):
        confirmation = messagebox.askyesno("Rejouer", "Voulez-vous rejouer ?")
        #Si confirmation = true , on continue le jeu et réinitialise
        if confirmation:
            self.label_tour.config(text=f"Tour du joueur : {joueur}")
            self.reinitialiser_jeu()
        #Sinon on ferme la fenetre
        else:
            self.quitter_jeu()

    #Méthode pour l'adversaire "robot"
    def jouer_robot(self):
        #Ici on identifie les mouvements possibles du "robot"
        mouvements_possibles = [(i, j) for i in range(3) for j in range(3) if self.boutons[i][j]["text"] == ""]
        #Si un movements est possibles
        if mouvements_possibles:
            #On choisit au hazard un mouvement pour le robot en fonction des mouvement possibles
            choix_robot = random.choice(mouvements_possibles)
            i, j = choix_robot
            #le texte du robot est déterminé comme "O"
            self.boutons[i][j].config(text="O")
            self.tour += 1
            #Vérification pour la victoire ou match nul
            if self.verifier_victoire():
                messagebox.showinfo("Fin de partie", "Le joueur Robot a gagné !")
                self.mettre_a_jour_score("Joueur 2")
                self.afficher_rejouer("Joueur 2")
            elif self.verifier_match_nul():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.afficher_rejouer("Joueur 2")

    #Méthode pour la mise à jour du score des joueurs ou du robot
    def mettre_a_jour_score(self, joueur):
        if joueur == "Joueur 1":
            self.score_joueur1 += 1
        elif joueur == "Joueur 2":
            self.score_joueur2 += 1
        elif joueur == "Robot":
            self.score_robot += 1

        self.label_score.config(text=f"Score : Joueur 1 - {self.score_joueur1} | Joueur 2 - {self.score_joueur2} | Robot - {self.score_robot}")

    #méthode redirection vers les règles du jeu
    def regle(self):
        messagebox.showinfo("Redirection", "Vous allez être redirigé vers les règles du jeu Tic Tac Toe")
        webbrowser.open("https://boulderbugle.com/tic-tac-toe-regle-de-jeu-2Rg9TiU5")

    #Méthodes dîtes "main", c'est là où on appelle la plupart des méthodes pour que le programme tourne et/ou fonctionne
    def main(self):

        choix_adversaire = messagebox.askquestion("Choix de l'adversaire", "Voulez-vous jouer contre un robot ?", icon='question')
        #En fonction de la réponse, détermination de l'adversaire
        self.adversaire = "robot" if choix_adversaire == "yes" else "humain"

        style = ttk.Style()
        #Configuration des styles généraux des boutons
        style.configure("TButton", font=('Helvetica', int(-self.fenetre.winfo_height() // 20), 'bold'), padding=5)
        style.configure("TButtonRegle.TButton", font=('Helvetica', int(-self.fenetre.winfo_height() // 50)), padding=0)

        #Création d'une grille dans la page pour l'affichage
        for i in range(3):
            self.fenetre.grid_rowconfigure(i, weight=1)
            self.fenetre.grid_columnconfigure(i, weight=1)
            #Création de la grille des boutons
            for j in range(3):
                bouton = ttk.Button(self.fenetre, text="", command=lambda i=i, j=j: self.bouton_clic(i, j), style="TButton")
                bouton.grid(row=i, column=j, sticky="nsew")
                self.boutons[i][j] = bouton

        #Initialisation des boutons
        bouton_quitter = ttk.Button(self.fenetre, text="Quitter", command=self.quitter_jeu, style="TButton")
        bouton_quitter.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

        self.label_tour.grid(row=4, column=0, columnspan=3, pady=10)
        self.label_score.grid(row=5, column=0, columnspan=3, pady=10)

        bouton_info = ttk.Button(self.fenetre, text="Règle du jeu", command=self.regle, style="TButtonRegle.TButton")
        bouton_info.grid(row=6, column=0, columnspan=3, pady=5, sticky="nsew")

        self.fenetre.mainloop()
        

#Instanciation de la classe
jeu = TicTacToe()
#Appelle de la méthode main pour commencer le jeu
jeu.main()
