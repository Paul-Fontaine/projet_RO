from classes_3d import test_shelves_drawers_3d_first_fit
from marchandises_ import marchandises

if __name__ == '__main__':
    test_shelves_drawers_3d_first_fit(sorted(marchandises, key=lambda m: (m.h, m.w, m.l), reverse=True))
