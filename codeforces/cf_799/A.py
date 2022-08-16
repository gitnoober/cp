from collections import defaultdict


for _ in range(int(input())):
    a = list(map(int, input().split()))

    def my(a):
        a = [(i,j) for i,j in enumerate(a)]
        a.sort(key = lambda x : -x[-1])
        for i in range(4):
            if a[i][0] == 0 :
                return i

    def his(a):
        x=a[0]
        a.sort()
        return 3-a.index(x)

    x,y = my(a), his(a)
    if x != y :
        print(x,y)

# for _ in range(int(input())):
#   n = int(input())
#   a = list(map(int, input().split()))
#   # print(len(set(a)))
#   elements = 0
#   d = defaultdict(int)
#   for i in a :
#       d[i]+=1

#   for i in d :
#       elements += max(0, d[i] - 1)

    
#   print(len(d) - (elements % 2))
