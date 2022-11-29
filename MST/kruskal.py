# union find
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


#  MST
def kruskal(edges, parent):
    cost = 0
    edges.sort()
    length = len(edges)
    for i in range(length):
        weight, n1, n2 = edges[i]
        if find(n1, parent) != find(n2, parent):
            union(n1, n2, parent)
            cost += weight
    return cost
