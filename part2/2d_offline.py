import time
from classes_2d import shelf_2d_bin_packing, plot_bins_2d
from marchandises_ import *


def test_shelf_offline():
    s = time.time()
    sorted_marchandises = sorted(marchandises, key=lambda m: (m.w, m.l), reverse=True)
    bins = shelf_2d_bin_packing(sorted_marchandises)
    d = time.time() - s
    n = len(bins)

    # for bin in bins:
    #     print(bin)
    # print(f"{n} bins in {d} s")
    plot_bins_2d(bins, d)
    print()


if __name__ == '__main__':
    test_shelf_offline()
