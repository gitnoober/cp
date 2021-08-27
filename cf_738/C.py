import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]



sys.setrecursionlimit(100000)
def DFS(u,vis,adj,path):
	vis[u] = True
	path.append(u)
	for i in range(n+1):
		if adj[u][i] and not vis[i]:
			DFS(i, vis, adj,path)


for _ in range(*maps()):
	n, = maps()
	a = [*maps()]
	if a[0] == 1:
		print(n+1 ,end=' ')
		print(*range(1 , n+1))
		continue

	if a[-1] == 0:
		print(*range(1 , n + 2))
		continue

	for i in range(n-1):
		if a[i] == 0 and a[i+1] == 1:
			print(*range(1, i+2) , n+1 , *range(i+2 , n+1))
			break
		