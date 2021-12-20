
def floyd_warshall(edges, n):
	dist = [[0 if i == j else float('inf')] for j in range(n)]
	pred = [[None]*n for _ in range(n)]

	for u , v , d in edges:
		pred[u][v] = u
		dist[u][v] = d

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i][k] + dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
					pred[i][j] = pred[k][j]
					
	return dist , pred



