INF = 100000 + 1
parent = [i for i in range(INF)]
# union find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


#  MST
def kruskal(edges):
    cost = 0
    edges.sort()
    length = len(edges)
    for i in range(length):
        weight, n1, n2 = edges[i]
        if find(n1) != find(n2):
            union(n1, n2)
            cost += weight
    return cost
