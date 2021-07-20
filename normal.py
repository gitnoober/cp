import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = 1<<60, 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline
from functools import reduce
def maps():return map(int , input().split())

#THINK ABOUT THE EDGE CASES ..........

"""
for _ in range(int(input())):
	n = int(input()) ; a = list(maps())
	pos = n- 1
	while pos>0 and a[pos-1]>=a[pos]:pos-=1
	while pos>0 and a[pos-1]<=a[pos]:pos-=1
	print(pos)

longest suffix which is sorted either increasing or decreasing doesn't matter
"""

"""

for _ in range(int(input())):
	n = int (input())
	t = [98]*51
	for i in [0] + list(maps()):
		t[i]^=1
		print(''.join(map(chr,t)))

"""

"""
for _ in range(int(input())):
	n = int(input()) ; a = list(input().rstrip('\n'))
	i,j =0,n-1
	while i<n and a[i] =='0':i+=1
	while j >=0 and a[j] =='1':j-=1
	for k in range(i,j):
		a[k] ='-1'
	print(''.join(list(filter(lambda x : (x!='-1') ,a))))
trailing 0's + 0(answer of the string b/w the trailing 0's and 1's) and 1's 
"""


def A():
	for _ in range(int(input())):
		n , k = maps() ; S = '0'*k + input().rstrip('\n') +'0'*k
		su = sum(max(0,(len(s)-k)//(k+1)) for s in S.split('1'))
		print(su)



def B():
	for _ in range(int(input())):
		n = int(input()) ; a = list(maps()) ;ans =[]
		for i in range(n):
			if i ==0 or i == n-1 or ((a[i-1] < a[i])!=(a[i] < a[i+1])):
				ans.append(a[i])
		print(len(ans)) ; print(*ans)

def C():
	for _ in range(int(input())):
		n , x =maps() ; a= list(maps()) ; e =o=0
		for i in a:e , o = (e ,o+1) if i %2 else (e+1 ,o)
		if o ==0:print('No') ; continue
		print('Yes') if (x % 2 and ( ( o % 2 ) or (o%2 ==0 and o-1 >=x))) else print('No') if e ==0 else (print('Yes') if (e%2 and e + (o - (1 if o%2==0 else 0)) >=x) or (o>=x) else print('Yes') if (e + (o - (0 if o%2 else 1)) >=x) or ((e -1) +o>=x) else print('No')) if x %2 else print('Yes') if (e % 2 and o % 2 ) or (o %2 ==0 and o + (e - (1 if e%2==0 else 0)) >=x) or (e %2 ==0 and e + (o - (1 if o%2==0 else 0)) >=x) else print('No')

def D():
	n , m = maps()
	if n == m:
		print(0),exit()
	ans = 0
	while m!=n:
		if m < n:
			ans+= (n-m) ; break
		else:
			if m % 2==0:
				m//=2
			else:
				m+=1
			ans+=1
	print(ans)
	"""
	make the question in another way, that is if we start from m how can we get to n ,
	if we apply "divide by 2" and "add 1 " operations ,if m is even we divide by 2 and if it's odd we add one
	that only if m > n else all we need to do is add m-n
	"""


def E():
	n , t = maps() ;a = list(maps())
	ans = s = idx = 0
	for i in a:
		s+=i
		if s > t:
			s-=a[idx]
			idx+=1
	print(n-idx)


def F():
	n , m = maps()
	t =n-m +1; kmax = t*(t-1)//2
	x = n//m
	print(m*x*(x-1)//2 + x*(n%m), kmax)


F()
