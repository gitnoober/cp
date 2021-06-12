import os , sys,time, collections as c , math as mt, pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
import bisect
input = sys.stdin.readline

def maps():return map(int , input().split())

N = 1000
arr,i=[True]*(N+1),2
arr[0]=arr[1] =False
while i * i <= N+1:
	if arr[i]:
		for j in range(2*i , N+1 , i):
			arr[j]= False
	i+=1
for i in range(1 , N+1):
	arr[i]+=arr[i-1]

for i in range(int(input())):
	n = int(input())
	if n <=3:
		print(arr[n] - arr[n//2]) ; continue
	print(arr[n] - arr[n//2] + 1)

#Because the prime numbers less than n/2 + 1 are grouped under 2 and the prime numbers more than n/2 are not grouped because they are the largest multiple from [2,N]


