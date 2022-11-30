parent = [i for i in range(100001)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# def union(x, y):