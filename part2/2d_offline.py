import random
import time
from classes import Bin
from marchandises_ import *


# it's a first fit algorithm,
# best fit could be more optimal but more computationnaly expensive
# if you want a really optimal solution, use the guillotine method
def shelf_2d_bin_packing(marchandises):
    marchandises_ = sorted(marchandises, key=lambda m: m.w, reverse=True)  # sort by width
    # a best fit algorithm could be worth if the sshelves heights are well combined
    # the width of a shelf will be the width of its first item and won't change

    n_minimum_bins = round(sum(m.l*m.w for m in marchandises_) / (L*W)) + 1
    bins = [Bin() for _ in range(n_minimum_bins)]
    j = 0
    for bin in bins:
        while bin.add_marchandise(marchandises_[j]):
            j += 1

    for i, m in enumerate(marchandises_[j::-1]):
        # first try to add the marchandise in an existing shelf
        for bin in bins:
            can_add_in_shelf = False
            for shelf in bin.shelves:
                if shelf.can_fit(m):
                    can_add_in_shelf = True
                    shelf.add_marchandise(m)

            # need to create a new shelf
            if not can_add_in_shelf:
                candidates_bins = [bin for bin in bins if bin.can_add_shelf(m.w)]
                if len(candidates_bins):  # if a bin or more can add a new shelf
                    selected_bin = min(candidates_bins, key=lambda b: b.remaining_width)
                    selected_bin.add_marchandise(m)  # the creation of the new shelf is hidden in bin.add_marchandise()
                    break

                # no place in all shelves and can't add a new shelf in all bins -> create a new bin
                new_bin = Bin()
                if new_bin.add_marchandise(m):
                    bins.append(new_bin)
                    break
                else:
                    # in theory, it can't be trigerred with the data used
                    raise ValueError(f"the marchandise {m} doesn't fit in an empty bin !")

    return bins


def test_shelf_offline():
    s = time.time()
    bins = shelf_2d_bin_packing(marchandises)
    d = time.time() - s
    n = len(bins)

    for bin in bins:
        print(bin)
    print(f"{n} bins in {d} s")


if __name__ == '__main__':
    test_shelf_offline()
