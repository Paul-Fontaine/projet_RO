
from marchandises_ import *

def ajuste_fit(liste_marchandises, L):
    total =0
    for objet in liste_marchandises:
        total += objet.l
    borne_inf = int(total/L)+1
    print(borne_inf)
    marchandises_trie = sorted(liste_marchandises, key=lambda m: m.l, reverse=True)  # sort marchandises by their length

    remaining_space_in_bins = [L] * borne_inf
    nb_marchandise =0
    for i in range(borne_inf):
        remaining_space_in_bins[i] -= marchandises_trie[i].l
        nb_marchandise += 1
###première étape on rempli les wagons avec les (borne_inf)-ième premiers objets

    restes_liste = []
    indice_min_des_restes = 0

    while nb_marchandise<=100:
        min_des_restes = 100
        for i in remaining_space_in_bins:
            restes_liste.append(i - marchandises_trie[nb_marchandise].l)


        for j in range(borne_inf - 1):  # égal à len(restes_liste)
            if restes_liste[j] <= min_des_restes & restes_liste[j] >= 0:
                min_des_restes = restes_liste[j]
                indice_min_des_restes = j
        remaining_space_in_bins[indice_min_des_restes] -= marchandises_trie[nb_marchandise].l

        nb_marchandise+=1


    return remaining_space_in_bins




if __name__ == '__main__':
    print(ajuste_fit(marchandises, L))
