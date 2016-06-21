def gnome_sort(list_):
    a = list_[:]
    i = 0

    while True:
        if i == len(a) - 1:
            return a
        else:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

                if i - 1 >= 0:
                    i -= 1
            else:
                i += 1
