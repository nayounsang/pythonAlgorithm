def partition(lo, hi):
    p = lo
    for i in range(lo, hi):
        if arr[i] < arr[hi]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    arr[p], arr[hi] = arr[hi], arr[p]
    return p


def select(lo, hi, idx):
    pi = partition(lo, hi)
    if idx < pi:
        return select(lo, pi - 1, idx)
    elif idx > pi:
        return select(pi + 1, hi, idx)
    else:
        return arr[idx]
