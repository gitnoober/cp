from heapq import heappop , heappush

def dijkstra(graph , start):
    """
        Uses Dijkstra's algorithm to find the shortest distance from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist = [float('inf')]*n
    h = [(0 , start)]
    dist[start] = 0
    parents = [-1]*n

    while h:
        dis , u = heappop(h)
        if dis == dist[u]:
            for v , wt in graph[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    parents[v] = u
                    heappush(h , (dist[v] , v))

    return dist , parents


        


