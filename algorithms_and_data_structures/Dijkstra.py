from heapq import heappop, heappush


def dijkstra(graph, start):
    """
    Uses Dijkstra's algorithm to find the shortest distance from node start
    to all other nodes in a directed weighted graph.
    Time Complexity : O(V + ElogV)
    Fails with negative values and loops
    works with directed graphs

    Explanation on drawbacks:
    Since Dijkstra follows a Greedy Approach, once a node is marked as visited it cannot be reconsidered even if
    there is another path with less cost or distance.
    This issue arises only if there exists a negative weight or edge in the graph.

    """
    n = len(graph)
    dist = [
        float("inf")
    ] * n  # update distance if distance is less than infinity, basically greedy approach
    h = [(0, start)]
    dist[start] = 0
    parents = [-1] * n

    while h:
        dis, u = heappop(h)
        if dis == dist[u]:
            for v, wt in graph[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    parents[v] = u
                    heappush(h, (dist[v], v))

    return dist, parents
