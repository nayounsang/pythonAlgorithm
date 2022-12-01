def query(tree, left, right, node, a, b, func, default):
    """
    :param tree: 값을 구할 트리
    :param left,right: tree의 구간
    :param a,b: arr의 구간
    :param default: 만약 범위를 벗어났을 때 결과값에 영향없도록 하는 리턴 값
    query(tree,0,len(arr)-1,1,start_bound,right_bound,func,default)
    """
    if b < left or a > right:
        return default
    if a <= left and b >= right:
        return tree[node]
    mid = (left + right) // 2
    return func(query(tree, left, mid, node * 2, a, b, func, default),
                query(tree, mid + 1, right, node * 2 + 1, a, b, func, default))


def update(tree, left, right, node, idx, value, func):
    """
    :param tree: 적용할 세그먼트 트리
    :param idx: 값을 바꿀 arr의 인덱스
    :param value: arr의 idx를 무슨 값으로 바꿀 것인지
    :param func: 어떠한 작업을 할 것인지
    update(tree,0,len(arr)-1,1,idx,value,func)
    """
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
