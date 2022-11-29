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
