parent = [i for i in range(100001)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def downjump(x):
    """
    :return: we can jump to prev
    """
    p = find(x)
    if p == 0:  # first index of parent
        return False
    parent[p] = find(p - 1)
    return True


def upjump(x, limit):
    """
    :param limit: (last index of parent)
    :return: we can jump to nxt
    """
    p = find(x)
    if p == limit:
        return False
    parent[p] = find(p + 1)
    return True
