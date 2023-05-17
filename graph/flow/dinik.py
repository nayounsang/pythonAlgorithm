# const
from collections import deque

N = 10000
capacity = [[0] * (N + 1) for _ in range(N + 1)]
flow = [[0] * (N + 1) for _ in range(N + 1)]
INF = 1000000000
g = [[] for _ in range(N + 1)]
S, T = 1, 2


def reverse_edge(g): # if you need
    for node in range(1, N + 1):
        for n in g[node]:
            g[n].append(node)


def bfs():
    level = [-1] * N
    q = deque([S])
    level[S] = 0
    while q:
        node = q.popleft()
        for n in g[node]:
            if level[n] == -1 and capacity[node][n] - flow[node][n] > 0:
                level[n] = level[node] + 1
                q.append(n)
    return level


def dfs(node, f, level):
    if node == T:
        return f
    for n in g[node]:
        if level[n] == level[node] + 1 and capacity[node][n] - flow[node][n] > 0:
            ret = dfs(n, min(capacity[node][n] - flow[node][n], f), level)
            if ret > 0:
                flow[node][n] += ret
                flow[n][node] -= ret
                return ret
    return 0


def dinik():
    result = 0
    while True:
        level = bfs()
        if level[T] == -1:
            break
        while True:
            f = dfs(S, INF, level)
            if f == 0:
                break
            result += f
    return result
