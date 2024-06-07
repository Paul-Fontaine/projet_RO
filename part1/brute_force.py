import time
from items_dict import items_dict


# complexity O(2^n) : exponential
def make_combinations(items, W: float):
    combinations = []
    n = len(items)
    for i in range(2**n):
        combi = [items[j] for j in range(n) if (i >> j) & 1]  # use binary
        weight = sum([object['weight'] for object in combi])
        # I need to cut the overweighted solutions else my RAM has not enough place to store the 8 millions combinations
        if weight <= W:
            utility = sum([object['utility'] for object in combi])
            combinations.append({'objects': combi, 'weight': weight, 'utility': utility})
    return combinations


def find_max_utility(combinations):
    return max(combinations, key=lambda c: c['utility'])


def find_best_bag(items, W: float = 0.6):
    return find_max_utility(make_combinations(items, W+0.0001))


def test_brute_force(W: float = 0.6):
    """! brute force is quite slow. It can take up to few minutes if N or C are great"""
    s_time = time.time()
    best_bag = find_best_bag(items_dict, W)
    e_time = time.time()

    print(f"{e_time-s_time} s")
    for object in best_bag['objects']:
        print(object)
    print(f"poids : {best_bag['weight']}")
    print(f"utilité : {best_bag['utility']}")


if __name__ == '__main__':
    for W in [1, 2, 3, 4]:
        test_brute_force(W)
