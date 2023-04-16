def make_space(N, value):
    cap = 1
    while cap < N:
        cap = cap << 1
    return [value] * (cap << 1)


def init(tree, arr, func, cap):
    for i in range(cap, cap + len(arr)):
        tree[i] = arr[i - cap]
    for i in range(cap - 1, 0, -1):
        tree[i] = func(tree[i << 1], tree[i << 1 | 1])


def update(tree, idx, value, func, cap):
    i = cap + idx
    tree[i] = value
    while i > 1:
        tree[i >> 1] = func(tree[i], tree[i ^ 1])
        i = i >> 1


def query(tree, start, end, func, cap, default):
    start, end = start + cap, end + cap
    result = default
    while start < end:
        if start & 1:
            result = func(result, tree[start])
            start += 1
        if not end & 1:
            result = func(result, tree[end])
            end -= 1
        start = start >> 1
        end = end >> 1
    if start == end:
        result = func(result,tree[start])
    return result
