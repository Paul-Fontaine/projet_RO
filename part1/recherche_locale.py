from items_dict import items_dict
import random


def sol_init(data, W):
    utility = 0
    masse_sac = 0
    compo_aleatoire = []
    print(data)
    new_objet_index_tab = data.copy()
    print(new_objet_index_tab)
    print(len(new_objet_index_tab))
    random.shuffle(new_objet_index_tab) #chaque indice va etre determiné aléatoirement
    print(new_objet_index_tab)
    print(len(new_objet_index_tab))

    compt=0
    while (masse_sac <= W):
        if (masse_sac + new_objet_index_tab[compt]['weight'] <= W):
            utility += new_objet_index_tab[compt]['utility']
            masse_sac += new_objet_index_tab[compt]["weight"]

            compo_aleatoire.append(new_objet_index_tab[compt])
    #on a créé une composition de sac aléatoire
        compt+=1
    return compo_aleatoire, utility

def sol_voisines(composition, score_utility, data):
    liste_solutions_voisines = [] #liste qui va contenir toutes les solutions voisine à composition
    liste_solutions_valides = []

    for i in range(5):#on va créer 5 solutions voisines
        index_to_change = random.randint(0, len(composition))
        new_objets_index = random.randint(0, 22)
        liste_solutions_voisines[i] = copy(composition)
        liste_solutions_voisines[i][index_to_change] = new_objets_index

        #on a créé une solution
        utility = 0
        masse_sac = 0
        for j in liste_solutions_voisines[i]:  # on parcours les objets de la solution actuelle
            masse_sac += data[j]["weight"]
        if (masse_sac <= W):  # si la masse est plus petite on calcul le total utilité
            for j in liste_solutions_voisines[i]:
                utility += data[j]["utility"]
            liste_solutions_valides.append([liste_solutions_voisines[i], utility])

        return liste_solutions_valides

# def best_of_voisines(liste_solutions_valides):
#
#     for i in liste_solutions_valides:
#         if i[1]>i≤


print(sol_init(items_dict[:10], 0.6))

best_compo, best_utility = sol_init(items_dict, 0.6) #on initialise la meilleure compo avec la compo aléatoire
