print("Bienvenue, cher candidat au Just Prix")
print("----------------------------------")
print("Le principe du jeu est simple, entrez un prix dans la console.\nSi le prix est correct, vous aurez gagné le just prix!\nA vous de jouer")
from random import randint
justprix=randint(1,100)
prixcandidat= 101
while justprix != prixcandidat:
    prixcandidat=input("Veuillez introduire un prix de 1 à 100\n")
    if  str.isnumeric(prixcandidat) == True:
        prixcandidat=int(prixcandidat)
        if justprix == prixcandidat:
            print("Félicitations!\nVous avez gagné le Just Prix.\nVoici votre Chèque d'1 millions d'euros")
            exit()
        elif justprix > prixcandidat:
            print("C'est plus. Veuillez recommencer.")
            
        else:
            print("C'est moins. Veuillez recommencer.")
            
    else : 
        print("L'entrée introduite n'est pas un nombre.Veuillez recommencer")

