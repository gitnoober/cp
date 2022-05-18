
class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
    	N = 10000
    	vis = {0}
    	forb = [False]*N
    	gr = [[] for _ in range(N)]
    	for i in range(N):
    		if i - b >= 0:
    			gr[i].append((i-b,0))
    		if i + a < N :
    			gr[i].append((i+a,1))

    	for j in forbidden:
    		forb[j] = True


    	q = [(0,0 ,-1)]
    	dist = [-1 for _ in range(N)]
    	dist[0] = 0

    	for i,dis,t in q :
    		for v,typ in gr[i]:
    			if v in vis or forb[v]:
    				continue

    			if typ == t == 0:
    				continue

    			q.append((v,dis+1,typ))
    			dist[v] = dis+1
    			vis.add(v)

    	return dist[x]





forbidden = [1998]
a = 1999
b = 2000
x = 2000
obj = Solution().minimumJumps(forbidden, a,b,x)
print(obj)
