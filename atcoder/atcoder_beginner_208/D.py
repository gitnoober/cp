import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = 1<<60 , 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.buffer.readline

def maps():return map(int , input().split())

#THINK ABOUT THE EDGE CASES ..........

n , m = maps() ; abc = [[*maps()] for _ in range(m)]
graph = [[maxx for __ in range(n)] for _ in range(n)] ; ans =0
for a ,b ,c in abc:
	graph[a-1][b-1] = c
for i in range(n):
	graph[i][i] = 0
for k in range(n):
	for i in range(n):
		for j in range(n):
			graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
			ans+=(0 if graph[i][j] == maxx else graph[i][j])
print(ans)