import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Marchandise:
    def __init__(self, name: str, length: int, width: int, height: int):
        self.name = name
        self.l = int(length)
        self.w = int(width)
        self.h = int(height)

    def __str__(self):
        return f"{self.l}, {self.w}, {self.h} : {self.name}"


L = 11583
W = 2294
H = 2569


marchandises = [
    Marchandise('Tubes acier', 10000, 1000, 500),
    Marchandise('Tubes acier', 9000, 2000, 700),
    Marchandise('Tubes acier', 7500, 1200, 400),
    Marchandise('Acide chlorhydrique', 1000, 1000, 1000),
    Marchandise('Godet pelleteuse', 2000, 2000, 1000),
    Marchandise('Rails ', 11000, 1000, 200),
    Marchandise('Tubes PVC', 3000, 2000, 600),
    Marchandise('Echaffaudage', 3000, 1300, 1800),
    Marchandise('Verre', 3000, 2100, 600),
    Marchandise('Ciment', 4000, 1000, 500),
    Marchandise('Bois vrac', 5000, 800, 1000),
    Marchandise('Troncs chênes', 6000, 1900, 1000),
    Marchandise('Troncs hêtres', 7000, 1600, 1500),
    Marchandise('Pompe à chaleur', 5000, 1100, 2300),
    Marchandise('Cuivre', 6000, 2000, 1400),
    Marchandise('Zinc', 5000, 800, 800),
    Marchandise('Papier', 4000, 1600, 600),
    Marchandise('Carton', 7000, 1000, 1300),
    Marchandise('Verre blanc vrac', 9000, 900, 2200),
    Marchandise('Verre brun vrac', 3000, 1600, 900),
    Marchandise('Briques rouges', 5000, 1100, 2400),
    Marchandise('Pièces métalliques', 6000, 1600, 1400),
    Marchandise('Pièces métalliques', 7000, 900, 1200),
    Marchandise('Pièces métalliques', 3000, 1600, 1900),
    Marchandise('Ardoises', 1000, 1800, 1000),
    Marchandise('Tuiles', 2000, 1200, 2300),
    Marchandise('Vitraux', 4000, 700, 1200),
    Marchandise('Carrelage', 6000, 1200, 2500),
    Marchandise('Tôles', 7000, 600, 1500),
    Marchandise('Tôles', 9000, 1700, 1000),
    Marchandise('Tôles', 6000, 1900, 1600),
    Marchandise('Tôles', 3000, 2200, 2200),
    Marchandise('Tôles', 3000, 500, 2200),
    Marchandise('Mobilier urbain', 4000, 700, 1900),
    Marchandise('Lin ', 5000, 2200, 700),
    Marchandise('Textiles à recycler', 6000, 1300, 2500),
    Marchandise('Aluminium', 6000, 1300, 1200),
    Marchandise('Batteries automobile', 7000, 1400, 2500),
    Marchandise('Quincaillerie', 6000, 1100, 1000),
    Marchandise('Treuil', 7000, 900, 1300),
    Marchandise('Treuil', 8000, 500, 500),
    Marchandise('Acier ', 8000, 900, 1700),
    Marchandise('Laine de bois', 8000, 900, 1800),
    Marchandise('Ouate de cellusose', 5000, 1700, 1200),
    Marchandise('Chanvre isolation', 2200, 1600, 1100),
    Marchandise('Moteur élecrique', 4200, 1500, 800),
    Marchandise('Semi conducteurs', 3700, 900, 1400),
    Marchandise('Semi conducteurs', 5600, 500, 1400),
    Marchandise('Semi conducteurs', 4900, 900, 2500),
    Marchandise('Semi conducteurs', 8700, 1300, 1300),
    Marchandise('Semi conducteurs', 6100, 2200, 2300),
    Marchandise('Semi conducteurs', 3300, 1800, 2300),
    Marchandise('Semi conducteurs', 2600, 1600, 2300),
    Marchandise('Semi conducteurs', 2900, 1600, 2000),
    Marchandise('Aluminium', 2000, 1100, 600),
    Marchandise('Aluminium', 3000, 600, 1200),
    Marchandise('Aluminium', 6000, 1000, 800),
    Marchandise('Aluminium', 5000, 1300, 600),
    Marchandise('Aluminium', 4000, 2100, 2100),
    Marchandise('Aluminium', 6000, 1500, 1900),
    Marchandise('Aluminium', 4000, 800, 2100),
    Marchandise('Aluminium', 2000, 2000, 2300),
    Marchandise('Aluminium', 4000, 1000, 1100),
    Marchandise('Aluminium', 6000, 1800, 1100),
    Marchandise('Lithium', 6000, 1900, 900),
    Marchandise('Lithium', 3000, 2000, 2200),
    Marchandise('Lithium', 4000, 1500, 900),
    Marchandise('Lithium', 4000, 2100, 2500),
    Marchandise('Lithium', 2000, 1200, 1500),
    Marchandise('Lithium', 6000, 1300, 2000),
    Marchandise('Lithium', 2000, 800, 1100),
    Marchandise('Contreplaqué', 4000, 1400, 2000),
    Marchandise('Contreplaqué', 5000, 600, 500),
    Marchandise('Contreplaqué', 5000, 600, 1800),
    Marchandise('Contreplaqué', 4000, 700, 1400),
    Marchandise('Contreplaqué', 6000, 500, 700),
    Marchandise('Contreplaqué', 3000, 1500, 1800),
    Marchandise('Contreplaqué', 3000, 1400, 2000),
    Marchandise('Contreplaqué', 3000, 2000, 2300),
    Marchandise('Contreplaqué', 5000, 1500, 700),
    Marchandise('Contreplaqué', 5000, 2200, 500),
    Marchandise('Contreplaqué', 6000, 1200, 1200),
    Marchandise('Poutre ', 5000, 800, 700),
    Marchandise('Poutre ', 3000, 500, 1900),
    Marchandise('Poutre ', 5000, 1400, 700),
    Marchandise('Poutre ', 6000, 700, 700),
    Marchandise('Poutre ', 6000, 1200, 2000),
    Marchandise('Poutre ', 3000, 1700, 1100),
    Marchandise('Poutre ', 5000, 1600, 2100),
    Marchandise('Pneus ', 3000, 1300, 1700),
    Marchandise('Pneus ', 4000, 1500, 1700),
    Marchandise('Pneus ', 3000, 1500, 1900),
    Marchandise('Pneus ', 3000, 600, 1900),
    Marchandise('Pneus ', 5000, 1800, 500),
    Marchandise('Pneus ', 3000, 1800, 700),
    Marchandise('Pneus ', 4000, 1700, 1400),
    Marchandise('Pneus ', 4000, 1500, 500),
    Marchandise('Pneus ', 2000, 2100, 1800),
    Marchandise('Pneus ', 2000, 700, 1100),
    Marchandise('Pneus ', 6000, 1200, 1300)
]
