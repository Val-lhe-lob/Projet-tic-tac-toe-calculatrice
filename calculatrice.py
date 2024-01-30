def evaluer_expression(expression):
    try:
        # Utilisation de la fonction eval pour évaluer l'expression
        resultat = eval(expression)
        return resultat
    except Exception as e:
        return f"Erreur : {str(e)}"

def est_caractere_valide(caractere):
    # Vérifier si le caractère est un chiffre, une opération ou un espace
    chiffres_et_operations = "0123456789+-/. "
    return caractere in chiffres_et_operations

while True:
    # Demander à l'utilisateur d'entrer l'expression mathématique
    expression = input("Entrez une expression mathématique (par exemple, 1/26+5*9-9+36): ")

    # Vérifier si tous les caractères de l'expression sont valides
    if all(est_caractere_valide(c) for c in expression):
        # Évaluer l'expression et afficher le résultat
        resultat = evaluer_expression(expression)
        print(f"Le résultat de l'expression est : {resultat}")
    else:
        print("Erreur : Expression invalide. Veuillez entrer une expression mathématique valide.")

    # Demander à l'utilisateur s'il souhaite effectuer une autre opération
    continuer = input("Voulez-vous effectuer une autre opération? (oui/non): ").lower()
    if continuer != 'oui':
        break 