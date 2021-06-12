import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n , k = maps()
	s = [int(i) for i in input().rstrip('\n')]
	k,d,ans,f = list(maps()),[0]*n,[],0
	for i in range(n-1):
		if s[i]!=s[i+1]:
			d[i+1]=1;f+=1
		else:
			d[i+1]=2;f+=2
	# print(d)
	for i in k:
		idx = i-1
		s[idx]^=1
		if idx+1<n :
			if s[idx]!=s[idx+1]:
				f-=d[idx+1]
				d[idx+1]=1
			else:
				f-=d[idx+1]
				d[idx+1]=2
			f+=d[idx+1]

		if idx -1 > -1 :
			if s[idx]!=s[idx-1]:
				f-=d[idx]
				d[idx]=1
			else:
				f-=d[idx]
				d[idx]=2
			f+=d[idx]
		print(f)

