deep = [0] * (N + 1)  # deep[node]: most deep dist of node
dp = [[] for _ in range(N + 1)]  # dp[node] : (dist,son)


def treedp(node, par):  
    value = 0
    for n in tree[node]:
        if n == par:
            continue
        v = treedp(n, node) + 1
        value = max(value, v)
        if not dp[node]:
            heappush(dp[node], (v, n))
        elif v > dp[node][0][0]:
            heappop(dp[node])
            heappush(dp[node], (v, n))
    deep[node] = value
    return value


def toposort(root):
    q = deque([(root,0)])
    rvs = [[] for _ in range(N+1)]
    indeg = [0] * (N + 1)
    while q:
        node,par = q.popleft()
        for n in tree[node]:
            if n == par:
                continue
            q.append((n,node))
            rvs[n].append(node)
            indeg[node] += 1
    q = deque([])
    for n in range(1,N+1):
        if indeg[n] == 0:
            q.append(n)
    while q:
        node = q.popleft()
        for n in tree[node]:
            indeg[n] -= 1
            if indeg[n] == 0:
                q.append(n)
            v = deep[node] + 1
            deep[n] = max(deep[n],v)
            if not dp[n]:
                heappush(dp[n], (v, node))
            elif v > dp[n][0][0]:
                heappop(dp[n])
                heappush(dp[n], (v, node))


def farthest():
    treedp(1, 0)
    q = deque([1])
    up = [0] * (N + 1)
    max_dist = [-1] * (N + 1) 
    max_dist[1] = deep[1]
    while q:
        node = q.popleft()
        for n in tree[node]:
            if max_dist[n] > 0:
                continue
            d = deep[n]  # longest of subtree
            u1 = up[node] + 1  # up[par] + 1
            u2 = 0 # most deep of node
            for vv, nn in dp[node]:
                if nn != n:
                    u2 = max(u2, vv + 1) 
            up[n] = max(u1, u2)
            max_dist[n] = max(up[n], d) 
            q.append(n)
    return max_dist
