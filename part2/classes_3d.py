from marchandises_ import *
import time


class Bin:
    def __init__(self):
        self.shelves = []
        self.remaining_height = H  # H - sum of shelves heights

    def can_add_shelf(self, shelf_height):
        return shelf_height < self.remaining_height

    def add_marchandise(self, m:Marchandise) -> bool:
        # try to add the marchandise in the existing shelves
        for shelf in self.shelves:
            if shelf.can_fit(m):
                shelf.add_marchandise(m)
                self.remaining_height = H - sum(s.height for s in self.shelves)
                return True

        # if the marchandise has not been added in an existing shelf,
        # and there is no more width in the bin we cannot add this marchandise
        if not self.can_add_shelf(m.h):
            return False

        # the marchandise has not been added to an existing shelf,
        # and we can add a new shelf with this marchandise
        new_shelf = Shelf(self.remaining_height)
        new_shelf.add_marchandise(m)
        # if a new shelf is added the previous one can't extend
        if self.shelves:
            self.shelves[-1].max_height = self.shelves[-1].height
        self.shelves.append(new_shelf)
        self.remaining_height -= new_shelf.height
        return True

    def __str__(self):
        str = ""
        for shelf in self.shelves:
            str += f"{shelf}\n------------------------------------------\n"
        str += "\n\n______________________________________________________________________________________________\n\n"
        return str


class Shelf:
    def __init__(self, max_height):
        self.max_height = max_height  # the height available in the bin, if an item is too tall it goes in a new bin
        self.height = 0
        self.remaining_width = W
        self.drawers = []

    def can_fit(self, m: Marchandise):
        if m.h > self.max_height:
            return False
        for drawer in self.drawers:
            if drawer.can_fit(m) or self.can_add_drawer(m.w):
                return True
        return False

    def can_add_drawer(self, drawer_width):
        return drawer_width < self.remaining_width

    def add_marchandise(self, m: Marchandise) -> int:
        # try to add the marchandise in the existing drawers
        for drawer in self.drawers:
            if drawer.can_fit(m):
                drawer_width_increase = drawer.add_marchandise(m)
                self.remaining_width -= drawer_width_increase
                self.height = max(d.height for d in self.drawers)
                return True

        # if the marchandise has not been added in an existing drawer,
        # and there is no more width in the shelf we cannot add this marchandise
        if not self.can_add_drawer(m.w):
            return False

        # the marchandise has not been added to an existing drawer,
        # and we can add a new drawer with this marchandise
        new_drawer = Drawer(self.remaining_width)
        new_drawer.add_marchandise(m)
        # if a new drawer is added the previous one can't extend
        if self.drawers:
            self.drawers[-1].max_width = self.drawers[-1].width
        self.drawers.append(new_drawer)
        self.height = max(d.height for d in self.drawers)
        self.remaining_width -= new_drawer.width
        return True

    def __str__(self):
        str = ""
        for d in self.drawers:
            str += f"{d}\n"
        return str


class Drawer:
    def __init__(self, max_width):
        self.max_width = max_width
        self.width = 0
        self.height = 0
        self.remaining_length = L
        self.marchandises = []

    def can_fit(self, m: Marchandise):
        if m.w > self.max_width:  # marchandise too wide
            return False
        if m.l > self.remaining_length:  # marchandise too long
            return False
        return True

    def add_marchandise(self, m: Marchandise) -> (int, int):
        self.marchandises.append(m)
        self.remaining_length -= m.l
        # check if the marchandise increase width and height
        d_w = max(m.w - self.width, 0)
        d_h = max(m.h - self.height, 0)
        self.width += d_w
        self.height += d_h
        return d_w

    def __str__(self):
        str = ""
        for m in self.marchandises:
            str += f"{m.name}, "
        return str


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


def test_shelves_drawers_3d_first_fit(marchandises):
    # random.shuffle(marchandises)
    s = time.time()
    bins = shelves_drawers_3d_first_fit(marchandises)
    d = time.time() - s
    n = len(bins)

    if n > 24:
        plot_bins_3d(bins, d, nrows=5)
    plot_bins_3d(bins, d)


def plot_bins_3d(bins, time, nrows=4):
    # Create a figure and a grid of subplots
    ncols = 6
    n_axes = nrows*ncols
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 21))

    # Flatten the axes array for easier iteration
    axes = axes.flatten()

    # Add the rectangles to each subplot
    for i, bin in enumerate(bins):
        ax = axes[i]
        # subplot params
        ax.set_xlim(0, W)
        ax.set_ylim(0, H)
        ax.set_aspect('equal')
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        ax.set_title(f"Wagon {i}")
        colors = [
            'maroon', 'darkred', 'saddlebrown', 'sienna', 'brown', 'firebrick',
            'darkorange', 'chocolate', 'olive', 'darkolivegreen', 'forestgreen', 'green',
            'darkgreen', 'teal', 'darkcyan', 'navy', 'midnightblue', 'darkblue', 'blue',
            'indigo', 'purple', 'darkmagenta', 'crimson', 'darkslategray', 'darkslateblue',
            'mediumblue', 'mediumvioletred', 'royalblue', 'seagreen', 'steelblue', 'darkgoldenrod',
            'darkorchid', 'darkturquoise', 'deepskyblue', 'dodgerblue', 'mediumseagreen',
            'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumaquamarine', 'orangered'
        ]

        # add rectangles
        current_x = 0
        current_y = 0
        for s in bin.shelves:
            for d in s.drawers:
                ax.add_patch(patches.Rectangle((current_x, current_y), d.width, d.height, linewidth=1, edgecolor='black', facecolor=random.choice(colors)))
                ax.text(current_x + d.width/2, current_y + d.height/2, f"{d.remaining_length}", ha='center', va='center', fontsize=6, color='white')
                current_x += d.width
            current_x = 0
            current_y += s.height

    ax = axes[len(bins)]
    ax.set_xlim(0, L)
    ax.set_ylim(0, W)
    ax.set_aspect('equal')
    ax.axis('off')
    fill_ratio = sum(m.l * m.w * m.h for m in marchandises) / (L * W * H * len(bins))
    ax.text(W / 2, H / 2, f"{len(bins)} wagons\n remplissage : {format(fill_ratio * 100, '.2f')} % \n {time} s",
            ha='center', va='center', fontsize=10, color='gray', alpha=1)

    # remove useless axes because we are too strong and don't need 24 bins
    for i in range(len(bins)+1, n_axes):
        fig.delaxes(axes[i])

    # plt.tight_layout()

    plt.show()
