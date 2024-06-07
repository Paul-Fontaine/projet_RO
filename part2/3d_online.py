import random
from classes_3d import test_shelves_drawers_3d_first_fit
from marchandises_ import marchandises

if __name__ == '__main__':
    random.shuffle(marchandises)  # -> 25 to 27 wagons. quite bad but it's a first fit with tight wagons
    test_shelves_drawers_3d_first_fit(marchandises)
