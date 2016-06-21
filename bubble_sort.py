def bubble_sort(list_):
    a = list_[:]
    for i in range(len(a)):
        for j in range(len(a) - (i + 1)):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
