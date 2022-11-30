def query(tree, left, right, node, a, b, func, default):
    if b < left or a > right:
        return default
    if a <= left and b >= right:
        return tree[node]
    mid = (left + right) // 2
    return func(query(tree, left, mid, node * 2, a, b, func, default),
                query(tree, mid + 1, right, node * 2 + 1, a, b, func, default))


def update(tree, left, right, node, idx, value, func):
    if idx < left or idx > right:
        return tree[node]
    if left == right:
        tree[node] = value
        return value
    mid = (left + right) // 2
    a = update(tree, left, mid, node * 2, idx, value, func)
    b = update(tree, mid + 1, right, node * 2 + 1, idx, value, func)
    tree[node] = func(a, b)
    return tree[node]
