#Ex 1

def nombre_eleves(tableau):
    nbr=0
    for i in tableau:
        if type(i)==str:
            nbr+=1
    return nbr

def test_nombre_eleves():
    assert nombre_eleves(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == 3
    assert nombre_eleves(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, 1, 3, 2, 10]) == 2
    assert nombre_eleves(["Harry Potter", 10, 5, 8, 1, "Cedric", "Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == 4
    print("Test nombre_eleves(): ok")

test_nombre_eleves()

#Ex 2

def eleves(tableau):
    tab_eleves=[]
    for i in tableau:
        if type(i)==str:
            tab_eleves.append(i)
    return tab_eleves

def test_eleves():
    assert eleves(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == ["Harry Potter", "Cedric Diggory", "Drago Malefoy"]
    assert eleves(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, 1, 3, 2, 10]) == ["Harry Potter", "Cedric Diggory"]
    assert eleves(["Harry Potter", 10, 5, 8, 1, "Cedric", "Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == ["Harry Potter", "Cedric", "Diggory", "Drago Malefoy"]
    print("Test eleves(): ok")
    
test_eleves()

#Ex 3

# Définition de la fonction lecture_fichier() qui prend en paramètre un nom de fichier et retourne un tableau de réponses. 
def lecture_fichier(nom_fichier):
    """
    Entrée: fichier contenant les réponses
    Renvoie: tableau avec le nom des élèves et leurs réponses
    """
    tab = [] # Créaton d'un tableau vide
    fichier = open(nom_fichier, "r") # Ouverture du fichier
    ligne = fichier.readline() # Lecture de la première ligne
    while ligne != "": # Boucle de lecture jusqu’à la fin du fichier
        ligne = ligne.strip() # Retirer les espaces et les retours à la ligne
        ligne = ligne.replace(":", "/") # Uniformiser les séparateurs
        temp = ligne.split("/") # Séparer les éléments
        tab.append(temp[0]) # Ajoute le premier élément de la ligne
        for x in temp[1:]: # Parcours le reste des éléments
                tab.append(int(x)) # Les ajoute sous la forme d'entiers
        ligne = fichier.readline() # Lecture de la ligne suivante
    fichier.close() # Fermeture du fichier
    return tab # Retour du tableau final

#Ex 4

def maison(tableau, indice):
    maxi=1+indice
    for i in range(1,5):
        if tableau[i+indice]>tableau[maxi]:
            maxi=i+indice
    if maxi-indice==1:
        return "Gryffondor"
    elif maxi-indice==2:
        return "Serdaigle"
    elif maxi-indice==3:
        return "Poufsouffle"
    else:
        return "Serpentard"

def test_maison():
    assert maison(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10], 0) == "Gryffondor"
    assert maison(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10], 5) == "Poufsouffle"
    assert maison(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10], 10) == "Serpentard"
    print("Test maison(): ok")

test_maison()

#Ex 5

def repartition(tableau):
    dic={}
    for i in range(len(tableau)):
        if type(tableau[i])==str:
            dic[tableau[i]]=maison(tableau,i)
    return dic

def test_repartion():
    assert repartition(["Harry Potter", 10, 5, 8, 1, "Cedric Diggory", 6, 7, 9, 4, "Drago Malefoy", 1, 3, 2, 10]) == {'Harry Potter': 'Gryffondor', 'Cedric Diggory': 'Poufsouffle', 'Drago Malefoy': 'Serpentard'}
    assert repartition(["Harry Potter", 10, 5, 8, 1, "Drago Malefoy", 1, 3, 2, 10, "Cedric Diggory", 6, 7, 9, 4]) == {'Harry Potter': 'Gryffondor', 'Drago Malefoy': 'Serpentard', 'Cedric Diggory': 'Poufsouffle'}
    assert repartition(["Drago Malefoy", 1, 3, 2, 10, "Cedric Diggory", 6, 7, 9, 4, "Harry Potter", 10, 5, 8, 1]) == {'Drago Malefoy': 'Serpentard', 'Cedric Diggory': 'Poufsouffle', 'Harry Potter': 'Gryffondor'}
    print("Test repartition(): ok")

test_repartion()

#Ex 6

def nb_erreurs(dict1, dict2):
    erreurs=0
    for i in dict1:
        if dict1[i] != dict2[i]:
            erreurs += 1
    return erreurs

def test_nb_erreurs():
    assert nb_erreurs({"Harry Potter": "Gryffondor", "Cedric Diggory": "Poufsouffle", "Drago Malefoy": "Serpentard"}, {"Cedric Diggory": "Serdaigle", "Drago Malefoy": "Gryffondor", "Harry Potter": "Gryffondor"}) == 2
    assert nb_erreurs({"Harry Potter": "Gryffondor", "Cedric Diggory": "Poufsouffle", "Drago Malefoy": "Serpentard"}, {"Drago Malefoy": "Serpentard", "Cedric Diggory": "Poufsouffle", "Harry Potter": "Gryffondor"}) == 0
    assert nb_erreurs({"Harry Potter": "Gryffondor", "Cedric Diggory": "Poufsouffle", "Drago Malefoy": "Serpentard"}, {"Harry Potter": "Serdaigle", "Cedric Diggory": "Serdaigle", "Drago Malefoy": "Serdaigle"}) == 3
    print("Test nb_erreurs(): ok")

test_nb_erreurs()
