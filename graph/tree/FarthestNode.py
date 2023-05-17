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
            u2 = 0  # node에서 가장 깊은 거리
            for vv, nn in dp[node]:
                if nn != n:
                    u2 = max(u2, vv + 1) 
            up[n] = max(u1, u2)
            max_dist[n] = max(up[n], d)  # 두가지중 큰 것이 답 
            q.append(n)
    return max_dist
