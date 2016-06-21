from random import shuffle


def bogosort(list_):
    a = list_[:]
    while True:
        if any(a[i] > a[i + 1] for i in range(len(a) - 1)):
            shuffle(a)
        else:
            return a
