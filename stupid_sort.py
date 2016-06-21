def stupid_sort(list_):
    a = list_[:]
    while True:
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                break
        else:
            return a
