import time
import timeit
from items_dict import items_dict_integers


class Noeud:
    def __init__(self, object, parent: "Noeud", depth: int = 0, prendre: bool = False):
        self.left = None
        self.right = None
        self.parent = parent
        self.object = object
        self.prendre = prendre
        self.depth = depth

    def __str__(self):
        return f"{self.object}"


class ArbreBinaire:
    def __init__(self, items, W: float = 0.6):
        self.W = W
        self.items = items  # liste des noms, poids et utilités des objets
        self.best_utility = 0
        self.best_noeud = None
        self.root = Noeud({'weight': 0, 'utility': 0}, parent=None)

    def make_tree(self, parent: Noeud):
        if parent.depth >= len(self.items):  # si on est arrivé en bas
            return

        # mise à jour de la borne inférieure
        current_utility = self.branch_utility(parent)
        if current_utility > self.best_utility:
            self.best_utility = current_utility
            self.best_noeud = parent

        # si les objets qu'ils restent à ajouter n'ont aucune chance
        # de dépasser la borne inférieure de l'arbre : on arrête
        if self.max_possible_branch_utility(parent) > self.best_utility:
            # si on dépasse le poids maximal on n'ajoute pas à gauche, mais quand même à droite
            # n+1 a peut-etre une masse trop grande, mais peut-etre pas n+2
            if self.branch_weight(parent) + self.items[parent.depth]['weight'] <= self.W:
                parent.left = Noeud(self.items[parent.depth], parent=parent, depth=parent.depth + 1, prendre=True)
                self.make_tree(parent.left)

            parent.right = Noeud(self.items[parent.depth], parent=parent, depth=parent.depth + 1)
            self.make_tree(parent.right)

    def branch_weight(self, noeud: Noeud):
        weight = 0
        while noeud.depth >= 1:
            if noeud.prendre:
                weight += noeud.object['weight']
            noeud = noeud.parent
        return weight

    def branch_utility(self, noeud: Noeud):
        utility = 0
        while noeud.depth >= 1:
            if noeud.prendre:
                utility += noeud.object['utility']
            noeud = noeud.parent
        return utility

    def max_possible_branch_utility(self, noeud: Noeud):
        utility = self.branch_utility(noeud)
        utility += sum([item['weight'] for item in self.items[noeud.depth::]])
        return utility

    def get_best_combi(self):
        best_combi = []
        noeud = self.best_noeud
        while noeud.depth >= 1:
            if noeud.prendre:
                best_combi.append(noeud.object)
            noeud = noeud.parent
        return best_combi


def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = f"{getattr(root, val)['weight']}, {getattr(root, val)['utility']}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = f"{getattr(root, val)['weight']}, {getattr(root, val)['utility']}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = f"{getattr(root, val)['weight']}, {getattr(root, val)['utility']}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = f"{getattr(root, val)['weight']}, {getattr(root, val)['utility']}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


def test_arbre(W: int = 60):
    """
    run 1000 simulations to get an execution time in ms :)
    """
    arbre = ArbreBinaire(items_dict_integers, W)
    arbre.make_tree(arbre.root)
    for object in arbre.get_best_combi():
        print(object)
    print()
    print(f"utility : {arbre.best_utility}")
    print()

    setup = """
from items_dict import items_dict_integers
from arbre import ArbreBinaire
    """
    code = """
arbre = ArbreBinaire(items_dict_integers)
arbre.make_tree(arbre.root)
best_combi = arbre.get_best_combi()
    """

    d = timeit.timeit(stmt=code, setup=setup, number=1000)
    print(d, "ms")  # 12.7 ms


def test_arbre_time(W: int = 60):
    s = time.time()
    arbre = ArbreBinaire(items_dict_integers, W)
    arbre.make_tree(arbre.root)
    d = time.time() - s
    # for object in arbre.get_best_combi():
    #     print(object)
    # print()
    print(f"W : {W/100}, utility : {arbre.best_utility/10}, temps : {d} s")
    # print()
    # print(d * 1000, "ms")


if __name__ == '__main__':
    for W in [60, 200, 300, 400, 500]:
        test_arbre_time(W)
