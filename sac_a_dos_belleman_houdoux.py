u = [49, 85, 16, 58, 32, 14, 17, 40, 58, 37, 78, 77, 85, 12, 10, 100, 70, 49, 7, 52, 19, 50, 36, 56, 54, 47, 55, 23, 38,
     5, 44, 32, 51, 7, 51, 41, 53, 4, 13, 17, 20, 48, 64, 33, 52, 29, 61, 70, 82, 5]
e = [24, 15, 6, 26, 24, 19, 26, 3, 18, 9, 19, 20, 7, 14, 26, 24, 24, 27, 25, 3, 23, 18, 14, 6, 11, 16, 3, 0, 2, 28, 26,
     11, 29, 16, 3, 16, 20, 19, 29, 26, 25, 14, 19, 27, 20, 27, 23, 22, 13, 12]


def utilite_max(u, e, C):
    def s(k, c):
        if c < 0:
            return -float("inf")
        elif k == 0:
            return 0
        else:
            if (k, c) not in Ds:
                Ds[(k, c)] = max(s(k - 1, c), s(k - 1, c - e[k - 1]) + u[k - 1])
            return Ds[(k, c)]

    Ds = {}
    return s(len(u), C)


def max_et_arg(liste):
    return (max(liste), liste.index(max(liste)))


def remplissage_optimal(u, e, C):
    def s(k, c):
        if c < 0:
            return (-float("inf"), None)
        elif k == 0:
            return (0, 0)
        else:
            if (k, c) not in Ds:
                Ds[(k, c)] = max_et_arg([s(k - 1, c)[0], s(k - 1, c - e[k - 1])[0] + u[k - 1]])
            return Ds[(k, c)]

    Ds = {}
    solution = []
    for k in range(len(u), 1, -1):
        if s(k, C)[1] == 1:
            solution.append(k - 1)
            C -= e[k - 1]
        solution.reverse()
    return solution.reverse()


print(remplissage_optimal(u, e, 0))