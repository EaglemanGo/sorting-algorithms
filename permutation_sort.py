from itertools import permutations


def permutation_sort(list_):
    a = list_[:]
    for i in permutations(a):
        if all(i[j] <= i[j + 1] for j in range(len(i) - 1)):
            return list(i)
