
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())
def f(ma_i,mi_i):
	x =min(ma_i, mi_i)
	if ma_i>x:
		q,w=ma_i-x,n-ma_i+1
		return x+ min(q,w)
	else:
		q,w=mi_i-x,n-mi_i+1
		return x+ min(q,w)

for _ in range(int(input())):
	n=int(input());a=list(maps())
	mi_i ,ma_i = a.index(min(a))+1 , a.index(max(a))+1
	lma ,rma= ma_i,n-ma_i+1
	lmi , rmi = mi_i, n-mi_i+1
	A =[lma , rma , lmi , rmi]
	idx= A.index(min(A))
	ans=A[idx]
	if idx % 2 == 0:
		if idx == 0:
			print(ans + min(lmi - ans , rmi))
		else:
			print(ans + min(lma - ans , rma))
	else:
		if idx == 1:
			print(ans + min(lmi ,  rmi -ans ))
		else:
			print(ans + min(lma , rma - ans))
