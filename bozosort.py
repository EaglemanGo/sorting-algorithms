from random import randint


def bozosort(list_):
    a = list_[:]
    while True:
        if any(a[i] > a[i + 1] for i in range(len(a) - 1)):
            x, y = randint(0, len(a) - 1), randint(0, len(a) - 1)
            a[x], a[y] = a[y], a[x]
        else:
            return a
