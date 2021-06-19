# Chuck Norris played the game of thrones and won.
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

def one(arr):
	n=len(arr)
	A=[0]*n
	for i in range(0,n-1 , 2):
		# print(i,"pp",A,arr,n,arr[i],arr[i+1])
		A[i],A[i+1]=arr[i+1],arr[i]
	return A
def two(arr):
	n=len(arr)
	A=[0]*n
	for i in range(n//2):
		# print( n//2 ,A,arr)
		A[i],A[n//2+i]=arr[n//2+i],arr[i]
	return A
def recur(arr, x,c,type):
	if arr == x:
		return c
	elif c > 2*len(arr):
		return maxx
	else:
		if type ==1 :
			arr = two(arr)
			return recur(arr, x, c+1, 2)
		else:
			arr = one(arr)
			return recur(arr, x, c+1, 1)

		

n=int(input())
a=list(maps());x=sorted(a)
if a == x:
	print(0)
else:
	A = one(a)
	B = two(a)
	ans = min(recur(A, x, 1, 1), recur(B, x, 1, 2))
	print(-1 if ans == maxx else ans)
