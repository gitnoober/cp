import os , sys,time, collections , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline
def maps():return map(int , input().split())

for _ in range(int(input())):
	n , L ,R = maps() ; c = list(maps()) ; cl , cr = [0]*(n+1) , [0]*(n+1)
	for i in range(n):
		if i < L:
			cl[c[i]]+=1
		else:
			cr[c[i]]+=1
	for i in range(n+1): # 0 dollars operation
		mn = min(cl[i], cr[i])
		cl[i]-=mn ; cr[i]-=mn
		L-=mn ; R-=mn
	ans = 0
	if L >= R:
		for i in range(n+1):
			mn = min(cl[i] - (cl[i]%2), L-R) #socks that can be converted to right
			ans+=mn//2 ; L-=mn
	else:
		for i in range(n+1):
			mn = min(cr[i] - (cr[i]%2) , R-L) #socks that can be converted to left
			ans+=mn//2 ; R-=mn
	ans+=abs(L-R)//2 + (L+R)//2 #(L+R)//2 (changing colors ) , abs(L-R)//2 (changing sides)
	print(ans)
