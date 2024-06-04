import time
from items_dict import items_dict


def make_combinations(items, W: float):
    combinations = []
    n = len(items)
    for i in range(2**n):
        combi = [items[j] for j in range(n) if (i >> j) & 1]  # use binary
        weight = sum([object['weight'] for object in combi])
        utility = sum([object['utility'] for object in combi])
        if weight <= W:
            combinations.append({'objects': combi, 'weight': weight, 'utility': utility})
    return combinations


def find_max_utility(combinations):
    return max(combinations, key=lambda c: c['weight'])


def find_best_bag(items, W: float = 0.6):
    return find_max_utility(make_combinations(items, W+0.0001))


s_time = time.time()
best_bag = find_best_bag(items_dict)
e_time = time.time()

print(f"{e_time-s_time} s")
for object in best_bag['objects']:
    print(object)
print(f"poids : {best_bag['weight']}")
print(f"utilité : {best_bag['utility']}")
