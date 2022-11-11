'''
Nom : Kuran
Prneom : Candas
Projet : note calculateur




'''
import time
from ast import If
from unittest import result

import progressbar

  
# Function to create  #coppy-paste lien: https://www.geeksforgeeks.org/progress-bars-in-python/
def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(10):
        time.sleep(0.1)
        bar.update(i)
          
# Driver's code
animated_marker()

# Constantes... 
NB_NOTES = 2
PONDERATION_NOTES = 0.4
PONDERATION_EXA = 0.6


def moyenne_ss_exa (liste_notes) :
    somme = 0
    for elem in liste_notes :
        somme += elem
    return somme / len(liste_notes)

def moyenne_finale (note, examen) :   
    return note*PONDERATION_NOTES + examen*PONDERATION_EXA



def affiche_moyenne(nom, module, liste_notes, moyenne, exemen=0) :
    #? pour ouvrir un fichier.txt
    liste = open("listeDeNotes.txt", "a")
    liste.write(f"\n -------- \n nom d'utilisateur :{nom}\n nom du module : {module}\n ")
    for i in range(len(liste_notes)) :
        liste.write(f"test{i+1}: {liste_notes[i]}\n")
    if exemen == 0:
        liste.write(f"moyenne : {moyenne:.1f}")
    else :
        #? inline if else
        statut = "echec" if moyenne < 4.0 else "succes"
        liste.write(f"examen : {exemen}\n moyenne : {moyenne:.1f}\n Statut : {statut}")
    liste.close()
    print(f"le fichier a été enregistré avec succès")
        
    
print("Note Calculateur")
print("40% de la note de la test et 60% de la note examen.")


nom = input("Veuillez entrer votre nom\n")
module = input("Veuillez entrer votre nom de module\n")

print(f"Salut {nom} \nSaisissez vos notes")

liste_notes = []

#? input pour obtenir la valeur de le note de l'utilisateurs
for i in range(NB_NOTES):
    liste_notes.append(float(input(f"test{i+1} : ")))
moyenne = moyenne_ss_exa(liste_notes)

examen = float(input("examen : "))


if examen == 0:    
    print(f"{nom} , moyenne de vos notes actuelles(pas de note d'examen) : {moyenne:.1f} , pour le module : {module}")
else :
    moyenne = moyenne_finale(moyenne, examen)
    if moyenne >= 4 :
        #? :.1f pour arrondir le ciffre
        print(f"{nom} , votre note: {moyenne:.1f} ====> vous avez réussi le module : {module}")
    #? pour notes echoue
    else:
        print(f"{nom} , votre note: {moyenne:.1f} ====> vous avez echoue au le module : {module}")
        
writeTxt = input("Voulez-vous sauvegarder les résultats? [y/n] ")

if writeTxt.lower() == "y":
    animated_marker()
    affiche_moyenne(nom, module, liste_notes, moyenne,examen)         
elif writeTxt.lower() == 'n':
    animated_marker()
    print(f"la transaction a été annulée")
else:
    animated_marker()
    print(f"vous avez fait une entrée non valide.La transaction a été annulée")






