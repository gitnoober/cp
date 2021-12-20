"""
	Algorithm for finding an MST

	Initially, you maintain two disjoint sets namely a set which contains of all the vertices in the MST and other 
	vertices which are not.

	1) You initialize a src  and,
	2) Choose a vertex which has the most minimum distance from that source
	3) Update all the distances from that chosen vertex if they are minimum that their previous distance (which was initially initialized to maximum int)


"""


def PrimeMST(n, adj):
    inf = float('inf')
    min_e = [[inf, -1] for _ in range(n)]
    selected = [False] * n
    min_e[0][0] = 0
    tot = 0
    mst_edges = []

    for i in range(n):

        v = -1
        for j in range(n):
            if not selected[j] and ((v == -1) or min_e[j][0] < min_e[v][0]):
                v = j

        if v == -1:
            return None, None

        selected[v] = True
        tot += min_e[v][0]

        if min_e[v][1] != - 1:
            mst_edges.append((v, min_e[v][1]))  # since it's unidirected

        for to in range(n):
            if adj[v][to] < min_e[to][0]:
                min_e[to] = [adj[v][to], v]

    return mst_edges, tot
