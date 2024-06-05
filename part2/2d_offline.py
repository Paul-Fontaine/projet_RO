import time

from marchandises_ import *


class Bin:
    def __init__(self):
        self.shelves = []
        self.remaining_width = W  # W - sum of the shelves width

    def can_add_shelf(self, shelf_width):
        return shelf_width < self.remaining_width

    def add_marchandise(self, m:Marchandise) -> bool:
        # try to add the marchandise in the existing shelves
        for shelf in self.shelves:
            if shelf.can_fit(m):
                shelf.add_marchandise(m)
                return True

        # if the marchandise has not been added in an existing shelf,
        # and there is no more width in the bin we cannot add this marchandise
        if not self.can_add_shelf(m.w):
            return False

        # the marchandise has not been added to an existing shelf,
        # and we can add a new shelf with this marchandise
        new_shelf = Shelf(self.remaining_width)
        new_shelf.add_marchandise(m)
        self.shelves.append(new_shelf)
        self.remaining_width -= new_shelf.width
        return True


class Shelf:
    def __init__(self, max_width):
        self.max_width = max_width  # the height available in the bin, if an item is too tall it goes in a new bin
        self.width = 0
        self.remaining_length = L
        self.marchandises = []

    def can_fit(self, m: Marchandise):
        if m.w > self.max_width:  # if the shelf cannot increase its width because of bin max width
            return False
        if m.l > self.remaining_length:  # if the shelf is "full" for this marchandise
            return False
        return True

    def add_marchandise(self, m: Marchandise):
        self.marchandises.append(m)
        self.remaining_length -= m.l
        self.width = max(self.width, m.w)  # if the marchandise is the widest of the shelf


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
                raise ValueError(f"the marchandise {m} doesn't fit in an empty bin !")

    return bins


def test_shelf():
    s = time.time()
    bins = shelf_2d_bin_packing(marchandises)
    d = time.time() - s
    n = len(bins)

    print(f"{n} bins in {d} s")


if __name__ == '__main__':
    test_shelf()
