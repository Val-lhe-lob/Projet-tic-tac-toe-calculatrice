import tkinter as tk
from tkinter import ttk, messagebox
import random
import time



class TicTacToe:
    #Initialisation des instances de la Class
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.geometry("400x350")
        self.tour = 0
        self.score_joueur1 = 0
        self.score_joueur2 = 0
        self.score_robot = 0
        self.boutons = [[None for j in range(3)] for i in range(3)] # Initialisation de la grille de boutons
        self.adversaire = ""
        self.label_tour = tk.Label(self.fenetre, text="Tour du joueur : Joueur 1", font=('Helvetica', 12, 'bold'))
        self.label_score = tk.Label(self.fenetre, text="Score : Joueur 1 - 0 | Joueur 2 - 0 | Robot - 0", font=('Helvetica', 12, 'bold'))

    def initialiser_jeu(self):
        for i in range(3):
            for j in range(3):
                self.boutons[i][j].config(text="")
        choix_adversaire = messagebox.askquestion("Choix de l'adversaire", "Voulez-vous jouer contre un robot ?", icon='question')
        self.adversaire = "robot" if choix_adversaire == "yes" else "humain"
        self.tour = 0
        self.label_tour.config(text="Tour du joueur : Joueur 1")


    def main(self):
        choix_adversaire = messagebox.askquestion("Choix de l'adversaire", "Voulez-vous jouer contre un robot ?", icon='question')
        self.adversaire = "robot" if choix_adversaire == "yes" else "humain"

        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', int(-self.fenetre.winfo_height() // 10), 'bold'), padding=5)

        for i in range(3):
            self.fenetre.grid_rowconfigure(i, weight=1)
            self.fenetre.grid_columnconfigure(i, weight=1)
            for j in range(3):
                bouton = ttk.Button(self.fenetre, text="", command=lambda i=i, j=j: self.bouton_clic(i, j), style="TButton")
                bouton.grid(row=i, column=j, sticky="nsew")

                self.boutons[i][j] = bouton

        bouton_quitter = ttk.Button(self.fenetre, text="Quitter", command=self.quitter_jeu, style="TButton")
        bouton_quitter.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

        self.label_tour.grid(row=4, column=0, columnspan=3, pady=10)
        self.label_score.grid(row=5, column=0, columnspan=3, pady=10)

        self.fenetre.mainloop()

    def bouton_clic(self, i, j):
        if self.boutons[i][j]["text"] == "":
            if self.tour % 2 == 0:
                self.boutons[i][j].config(text="X")
                joueur = "Joueur 1"
            else:
                self.boutons[i][j].config(text="O")
                joueur = "Joueur 2" if self.adversaire == "robot" else "Joueur 2"
            self.tour += 1

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
        else:
            messagebox.showerror("Case occupée", "Cette case est déjà occupée. Choisissez une autre case.")

    def verifier_victoire(self):
        for i in range(3):
            if self.boutons[i][0]["text"] == self.boutons[i][1]["text"] == self.boutons[i][2]["text"] != "":
                return True

        for j in range(3):
            if self.boutons[0][j]["text"] == self.boutons[1][j]["text"] == self.boutons[2][j]["text"] != "":
                return True

        if self.boutons[0][0]["text"] == self.boutons[1][1]["text"] == self.boutons[2][2]["text"] != "":
            return True
        if self.boutons[0][2]["text"] == self.boutons[1][1]["text"] == self.boutons[2][0]["text"] != "":
            return True

        return False

    def verifier_match_nul(self):
        for i in range(3):
            for j in range(3):
                if self.boutons[i][j]["text"] == "":
                    return False
        return True

    def quitter_jeu(self):
        self.fenetre.quit()

    def afficher_rejouer(self, joueur):
        confirmation = messagebox.askyesno("Rejouer", "Voulez-vous rejouer ?")

        if confirmation:
            self.label_tour.config(text=f"Tour du joueur : {joueur}")
            self.initialiser_jeu()
        else:
            self.fenetre.quit()

    def jouer_robot(self):
        mouvements_possibles = [(i, j) for i in range(3) for j in range(3) if self.boutons[i][j]["text"] == ""]
        if mouvements_possibles:
            choix_robot = random.choice(mouvements_possibles)
            i, j = choix_robot
            self.boutons[i][j].config(text="O")
            self.tour += 1

            if self.verifier_victoire():
                messagebox.showinfo("Fin de partie", "Le joueur Robot a gagné !")
                self.mettre_a_jour_score("Joueur 2")
                self.afficher_rejouer("Joueur 2")
            elif self.verifier_match_nul():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.afficher_rejouer("Joueur 2")

    def mettre_a_jour_score(self, joueur):
        if joueur == "Joueur 1":
            self.score_joueur1 += 1
        elif joueur == "Joueur 2":
            self.score_joueur2 += 1
        elif joueur == "Robot":
            self.score_robot += 1

        self.label_score.config(text=f"Score : Joueur 1 - {self.score_joueur1} | Joueur 2 - {self.score_joueur2} | Robot - {self.score_robot}")

jeu = TicTacToe()
jeu.main()
