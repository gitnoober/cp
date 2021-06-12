import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
    sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline

def maps():
    return map(int , input().split())

def dprint(*args):
    [print(i) for i in args]

# for _ in range(int(input())):
#   n = int(input()) ; a = list(maps())
#   s = sorted(set(a[i] - a[i-1] for i in range(1 , n )))
#   if len(s) <= 1:
#       print(0)
#   else:
#       if len(s)  == 2 and s[0] < 0 and s[1] > 0:
#           print(s[1] - s[0] , s[1]) if s[1] - s[0] > max(a) else print(-1)
#       else:
#           print(-1)
#           

# for _ in range(int(input())):
#   n = int(input()) ; a =list(maps())
#   fa , ca , d = 0 , 0 , c.defaultdict(int)
#   for i in range(n):
#       ca+=d[a[i]]
#       d[a[i]]+= i + 1
#       fa+=ca
#   print(fa)

"""

import heapq
n = int(input()) ; a = list(maps())
tot , h = 0 , []
heapq.heapify(h)
for i in a:
  tot+=i
  heapq.heappush(h, i)
  while tot < 0:
      tot-=heapq.heappop(h)
print(len(h))
greedily adding elements and removing the smallest elements to make the tot positive


"""


"""

for _ in range(int(input())):
    n , k = maps()
    a = list(maps())
    x , s= 0,a[0]
    for i in range(1,n):
        x = max(x, ((a[i]*100) - k*s)/k)
        s+=a[i]
    print(math.ceil(x))

"""



"""

Minimum number of swaps required to sort an array -
imagine the numbers of the array as a graph ,and the numbers whose positions need to switched with each other a cycle
so , the number of swaps required to sort the numbers in the cycle is size of the cycles - 1,and the total number of swaps is the summations of (cycle sizes -1)

a =[100 , 200 , 300,10,100] ; n = len(a)
arr =sorted([*enumerate(a)],key=lambda x : x[1]) #sorting it by items
vis =[False]*n
tot =0
for i in range(n):
    if vis[i] or arr[i][0]==i:
        continue
    j = arr[i][0]
    size = 0
    while not vis[j]:
        vis[j] = True
        size+=1
        j = arr[j][0]
    tot+=(size-1)
print(tot)

"""


# for _ in range(int(input())):
#     a ,b ,k =maps();A=list(maps());B=list(maps())
