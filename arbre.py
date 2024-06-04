from items_dict import items_dict

class Noeud :
    def __init__(self, poids, utility, liste_precedent, index):
        self.left = None
        self.right = None
        self.poids = poids
        self.utility = utility
        self.liste_precedent = liste_precedent
        self.index = index

    def __str__(self):  # méthode spéciale python qui permet de réaliser des conversions lorsque l’objet
        # est passé en paramètre de certaines fonctions
        return str(self.data)


class ArbreBinaire :
    def __init__(self, poids_sac_max, data, total_utility, index):
        self.poids_sac_max = poids_sac_max
        self.meilleure_valeur=0
        self.objets = data  # liste des poids, valeur
        self.meilleur_combinaison = []
        self.borne_inf = 0 #deviendra le meilleur
        self.borne_sup = total_utility
        self.index = index


    def explorer(self, noeud):
        if noeud.index >= len(self.objets):#si l'indice est plus grand que le nombre de d'objet
            return 1

        # Explorer le sous-arbre gauche (prendre l'objet)
        # self.objets[noeud.index] est le index-ème objet
        if noeud.poids + self.objets[noeud.index][0] <= self.poids_sac_max:
            left = Noeud( noeud.poids + self.objets[noeud.index][0],  #la gauche devient un noeud que l'on definit : left
                         noeud.valeur + self.objets[noeud.index][1],
                         noeud.liste_precedent.append(),
                         noeud.index + 1)
            if left.valeur > self.meilleure_valeur:
                self.meilleure_valeur = left.valeur
                self.meilleur_combinaison = left.objets_pris
            self.explorer(left)


        # Explorer le sous-arbre droit (ne pas prendre l'objet)
        droite = Noeud(noeud.niveau + 1, noeud.poids, noeud.valeur, noeud.objets_pris)
        self.explorer(right)




if __name__ == "__main__":








