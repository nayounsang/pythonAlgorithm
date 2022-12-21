import sys

N = 10000
sys.setrecursionlimit(N + 1)


def dfs(g, node, visit, stack):
    visit[node] = True
    for n in g[node]:
        if not visit[n]:
            dfs(g, n, visit, stack)
    stack.append(node)


def rvs_dfs(rvs, node, s, visit):
    visit[node] = True
    s.append(node)
    for n in rvs[node]:
        if not visit[n]:
            rvs_dfs(rvs, n, s, visit)


def kosaraju(g, rvs):
    scc = []
    stack = []
    visit = [False] * (N + 1)
    for node in range(1, N + 1):
        if not visit[node]:
            dfs(g, node, visit, stack)
    visit = [False] * (N + 1)
    while stack:
        tmp = []
        node = stack.pop()
        if not visit[node]:
            rvs_dfs(rvs, node, tmp, visit)
            scc.append(sorted(tmp))
    return scc
