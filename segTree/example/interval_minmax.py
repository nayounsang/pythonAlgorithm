def make_tree(value, N):
    cap = 1
    while cap < N:
        cap = cap << 1
    return [value] * (cap * 2)


def init(tree, arr, left, right, node, func):
    # init(tree,arr,0,len(arr)-1,1,func)
    if left == right:
        tree[node] = arr[left]
        return
    mid = (left + right) // 2
    init(tree, arr, left, mid, node * 2, func)
    init(tree, arr, mid + 1, right, node * 2 + 1, func)
    tree[node] = func(tree[node * 2], tree[node * 2 + 1])


def query(tree, left, right, node, a, b, func, default):
    """
    :param tree: 값을 구할 트리
    :param left,right: tree의 구간
    :param a,b: arr의 구간
    :param default: 만약 범위를 벗어났을 때 결과값에 영향없도록 하는 리턴 값
    query(tree,0,len(arr)-1,1,start_bound,end_bound,func,default)
    """
    if b < left or a > right:
        return default
    if a <= left and b >= right:
        return tree[node]
    mid = (left + right) // 2
    return func(query(tree, left, mid, node * 2, a, b, func, default),
                query(tree, mid + 1, right, node * 2 + 1, a, b, func, default))


# just temporary
arr = list(map(int, input().split()))
start_bound, end_bound = 2, 5
N = len(arr)

# build tree
max_tree = make_tree(0, N)
init(max_tree, arr, 0, N - 1, 1, max)
min_tree = make_tree(0, N)
init(min_tree, arr, 0, N - 1, 1, min)

# get value
max_value = query(max_tree, 0, len(arr) - 1, 1, start_bound, end_bound, max, 0)
min_value = query(min_tree, 0, len(arr) - 1, 1, start_bound, end_bound, min, float('inf'))
