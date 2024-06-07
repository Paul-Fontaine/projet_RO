from items_dict import items_dict
import time


def glouton(W: float = 0.6, items=items_dict):
    s = time.time()
    # sort itmes by the ratio utility²/weight
    items_sorted = sorted(items, key=lambda o: o['utility']*o['utility'] / o['weight'], reverse=True)

    bag = []
    bag_weight = 0
    bag_utility = 0
    # ajoute les premiers objets de la liste triée tant que le sac n'est pas trop lourd
    # cependant un objet avec un bon ratio peut être skip s'il est trop lourd pour le poids encore disponible
    for obj in items_sorted:
        if bag_weight + obj['weight'] <= W+0.0001:
            bag_weight += obj['weight']
            bag_utility += obj['utility']
            bag.append(obj)
        if abs(W-bag_weight) < 0.0001:  # le sac est plein
            break
    d = time.time() - s

    for obj in bag:
        print(obj)
    print()
    print("poids du sac : ", bag_weight)
    print("utilité du sac : ", bag_utility)
    print()
    print(d, "s")


if __name__ == '__main__':
    glouton()
