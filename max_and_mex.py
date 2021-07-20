
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())


for _ in range(int(input())):
	n , k = maps()
	a = sorted(maps())
	i = 0 ;ma ,ans = a[-1] , n
	d = {i:1 for i in a}
	for j in range(n):
		if k :
			if a[j] == i :
				i+=1
				continue
			x =math.ceil((i+ma)/2) 
			if x != i:
				k=0
				if x not in d:
					d[x]=1 ; ans+=1
				break
			else:
				ans+=1
				i+=1 ; k-=1
	print(k+ans)


