from collections import deque
from heapq import heappush, heappop


def dijkstra(graph, distance, start):
    distance[start] = 0
    heap = [(0, start)]  # dist, node
    while heap:
        dist, node = heappop(heap)
        for n, d in graph[node]:
            new = dist + d  # new distance
            if new < distance[n]:  # if improve
                heappush(heap, (new, n))
                distance[n] = new  # update shorter path


def chase_path(rvs, distance, s, e):
    # if undirected graph: u can just input raw graph
    # req hardcoding if path have its standards
    result = [e]
    cur = e
    while cur != s:
        for n,d in rvs[cur]:
            diff = distance[cur] - distance[n]
            if diff == d:
                cur = n
                result.append(n)
    return result[::-1]

