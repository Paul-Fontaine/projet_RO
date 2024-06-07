from items_dict import items_dict
import random

#retourne une solution définie aléatoirement
def sol_init(data, W):
    utility = 0
    masse_sac = 0
    compo_aleatoire = []

    new_objet_index_tab = list(range(len(data)))
    random.shuffle(new_objet_index_tab)
    print(new_objet_index_tab)

    compt = 0
    while compt < len(data) and (masse_sac + data[new_objet_index_tab[compt]]['weight'] <= W):
        index_objet = new_objet_index_tab[compt]
        utility += data[index_objet]['utility']
        masse_sac += data[index_objet]["weight"]
        compo_aleatoire.append(data[index_objet])
        compt += 1

    return compo_aleatoire, utility


# retourne une liste de solutions voisines de la solution initiale
def sol_voisines(composition, data, W):
    liste_solutions_voisines = [] #liste qui va contenir toutes les solutions voisine à composition
    liste_solutions_valides = [] #liste qui va contenir toutes les solutions voisine à composition et leurs utilités, dont le poids est inferieur à W

    for i in range(10): #on va créer 10 solutions voisines
        liste_solutions_voisines.append(composition.copy())
        index_to_change = random.randint(0, len(composition) - 1)
        new_objets_index = random.randint(0, len(data) - 1)
        liste_solutions_voisines[i][index_to_change] = data[new_objets_index]

        #on a créé une solution
        utility = 0
        masse_sac = 0
        for j in range(len(liste_solutions_voisines[-1])):  # on parcours les objets de la solution actuelle
            masse_sac += data[j]["weight"]

        if (masse_sac <= W):  # si la masse est plus petite on calcul le total utilité
            for j in range(len(liste_solutions_voisines[-1])):
                utility += data[j]["utility"]
            liste_solutions_valides.append([liste_solutions_voisines[-1], utility])

    return liste_solutions_valides



def best_of_voisines(liste_solutions_valides):
    best_utility = 0
    index_of_best_compo = 0
    for i in range(len(liste_solutions_valides)):
        if liste_solutions_valides[i][1]>best_utility:
            best_utility=liste_solutions_valides[i][1]
            index_of_best_compo = i

    return liste_solutions_valides[index_of_best_compo][0], best_utility



best_compo, best_utility = sol_init(items_dict, W=0.6)
#on initialise la meilleure compo avec la compo aléatoire

print("Meilleure utilité 1:", best_utility, "\nComposition 1:", best_compo)

for _ in range(6):
    best_compo_vois, best_utility_vois = best_of_voisines(sol_voisines(best_compo, items_dict, 0.6))
    if (best_utility_vois>=best_utility):
        best_compo = best_compo_vois
        best_utility = best_utility_vois
    print("Meilleure utilité :", best_utility, "\nComposition :", best_compo)








