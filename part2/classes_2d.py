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
                d = shelf.add_marchandise(m)
                self.remaining_width -= d
                return True

        # if the marchandise has not been added in an existing shelf,
        # and there is no more width in the bin we cannot add this marchandise
        if not self.can_add_shelf(m.w):
            return False

        # the marchandise has not been added to an existing shelf,
        # and we can add a new shelf with this marchandise
        new_shelf = Shelf(self.remaining_width)
        new_shelf.add_marchandise(m)
        # if a new shelf is added the previous one can't extend
        if self.shelves:
            self.shelves[-1].max_width = self.shelves[-1].width
        self.shelves.append(new_shelf)
        self.remaining_width -= new_shelf.width
        return True

    def __str__(self):
        str = ""
        for shelf in self.shelves:
            str += f"{shelf}\n"
        str += "\n"
        return str

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

    def add_marchandise(self, m: Marchandise) -> int:
        self.marchandises.append(m)
        self.remaining_length -= m.l
        d = m.w - self.width
        if d > 0:
            self.width += d
            return d
        return 0

    def __str__(self):
        str = ""
        for m in self.marchandises:
            str += f"{m.name}, "
        return str


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


def plot_bins_2d(bins, d):
    # Create a figure and a grid of subplots
    fig, axes = plt.subplots(nrows=7, ncols=5, figsize=(15, 21))

    # Flatten the axes array for easier iteration
    axes = axes.flatten()

    # Add the rectangles to each subplot
    for i, bin in enumerate(bins):
        ax = axes[i]
        # subplot params
        ax.set_xlim(0, L)
        ax.set_ylim(0, W)
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
            for m in s.marchandises:
                ax.add_patch(patches.Rectangle((current_x, current_y), m.l, m.w, linewidth=1, edgecolor='black', facecolor=random.choice(colors)))
                current_x += m.l
            current_x = 0
            current_y += s.width

    # print infos on the last subplot
    if len(bins) < 35:
        ax = axes[len(bins)]
        ax.set_xlim(0, L)
        ax.set_ylim(0, W)
        ax.set_aspect('equal')
        ax.axis('off')
        fill_ratio = sum(m.l*m.w for m in marchandises) / (L*W*len(bins))
        ax.text(L/2, W/2, f"{len(bins)} wagons\n remplissage : {format(fill_ratio*100, '.2f')} % \n {d} s", ha='center', va='center', fontsize=12, color='gray', alpha=1)

    # remove useless axes because we are too strong and don't need 35 bins
    for i in range(len(bins)+1, 35):
        fig.delaxes(axes[i])

    # Adjust layout
    plt.tight_layout()

    # Show plot
    plt.show()

