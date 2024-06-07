from marchandises_ import *


def best_fit(objects: 'List[Marchandise]'):
    n = len(objects)
    # I don't want to add bins dynamically
    # So I create the maximum number of bins and count the bins actually used at the end
    remaining_space_in_bins = [L]*n
    marchandises = sorted(objects, key=lambda m: m.l, reverse=True)  # sort marchandises by their length

    for m in marchandises:
        # find the bin the most filled that can contain m
        selected_bin = min((i for i in range(n) if remaining_space_in_bins[i] > m.l), key=lambda i: remaining_space_in_bins[i])
        remaining_space_in_bins[selected_bin] -= m.l

    n_bins_used = len([s for s in remaining_space_in_bins if s != L])
    return n_bins_used


if __name__ == '__main__':
    print(best_fit(marchandises))
