import random
import time

from classes_3d import Bin, marchandises, plot_bins_3d


def shelves_drawers_3d_first_fit(marchandises):
    bins = []

    for m in marchandises:
        placed: bool = False
        for bin in bins:
            if bin.add_marchandise(m):
                placed = True
                break

        if not placed:
            new_bin = Bin()
            if new_bin.add_marchandise(m):
                bins.append(new_bin)
            else:
                # in theory, it can't be trigerred with the data used
                raise ValueError(f"the marchandise {m} doesn't fit in an empty bin !")

    return bins


def test_shelves_drawers_3d_first_fit():
    # random.shuffle(marchandises)
    s = time.time()
    bins = shelves_drawers_3d_first_fit(sorted(marchandises, key=lambda m: (m.h, m.w, m.l), reverse=True))
    d = time.time() - s
    n = len(bins)

    plot_bins_3d(bins, d)


if __name__ == '__main__':
    test_shelves_drawers_3d_first_fit()
