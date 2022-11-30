def make_tree(value, N):
    cap = 1
    while cap < N:
        cap = cap << 1
    return [value] * (cap * 2)


def init(tree, arr, left, right, node, func):
    if left == right:
        tree[node] = arr[left]
        return
    mid = (left + right) // 2
    init(tree, arr, left, mid, node * 2, func)
    init(tree, arr, mid + 1, right, node * 2 + 1, func)
    tree[node] = func(tree[node * 2], tree[node * 2 + 1])