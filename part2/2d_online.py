import random
import time
from classes import Bin
from marchandises_ import *


# it's a first fit algorithm, best fit could be more optimal but if a really optimal solution use the guillotine method
def shelf_2d_bin_packing(marchandises):
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


def test_shelf_online():
    # random.shuffle(marchandises)  # produces 30 to 32 bins
    s = time.time()
    bins = shelf_2d_bin_packing(marchandises)
    d = time.time() - s
    n = len(bins)

    # for bin in bins:
    #     print(f"remaining_width = {bin.remaining_width}")
    #     print(bin)
    # print(f"{n} bins in {d} s")
    plot_bins(bins)


if __name__ == '__main__':
    test_shelf_online()
