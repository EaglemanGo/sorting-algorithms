def stooge_sort(list_):
    a = list_[:]
    x, y = 0, len(a) - 1

    def sort(l, m):
        nonlocal a

        if a[l] > a[m]:
            a[l], a[m] = a[m], a[l]

        if m - l > 1:
            n = (m - l + 1) // 3

            sort(l, m - n)
            sort(l + n, m)
            sort(l, m - n)

        return a

    return sort(x, y)
