N = 10000


def bellmanford(edge, start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    for node in range(1, N + 1):
        for a, b, w in edge:
            tmp = distance[a] + w
            if tmp < distance[b] < float('inf'):
                if node == N:
                    return []  # negative cycle if not return value
                distance[b] = tmp
    return distance
