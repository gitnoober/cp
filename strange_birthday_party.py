
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

#think about the edge cases 

for _ in range(int(input())):
	n , m = maps() ; a = sorted(maps() , reverse=True) ; b = list(maps()) ; ans =0
	j = 0
	for i in a:
		if i >= j+1 and j < n:
			if b[i-1] <= b[j]:
				ans+=b[i-1]
			else:
				ans+=b[j] ; j+=1
		else:
			ans+=b[i-1]
	print(ans)

