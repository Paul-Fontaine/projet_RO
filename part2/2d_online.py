import random
import time
from classes_2d import plot_bins_2d, shelf_2d_bin_packing
from marchandises_ import *


def test_shelf_online():
    random.shuffle(marchandises)  # produces 33 to 35 bins
    s = time.time()
    bins = shelf_2d_bin_packing(marchandises)
    d = time.time() - s
    n = len(bins)

    # for bin in bins:
    #     print(f"remaining_width = {bin.remaining_width}")
    #     print(bin)
    # print(f"{n} bins in {d} s")
    plot_bins_2d(bins, d)


if __name__ == '__main__':
    test_shelf_online()
