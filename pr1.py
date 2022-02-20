from collections import defaultdict, deque
from math import log2, ceil
for _ in range(int(input())):
    n,k = map(int, input().split())
    taken = defaultdict(list)
    bit_d = defaultdict(deque)
    if k == 0 :
        vis = set()
        ans = [(1,2)]
        vis.add(1)
        vis.add(2)
        for x in range(1,n):
            if x in vis:
                continue
            y = 0
            v = ceil(log2(x)) if x > 0 else 1
            for j in range(v,-1,-1):
                if (1<<j)&x:
                    continue
                y |= (1<<j)
            if y < n :
                vis.add(y)
                vis.add(x)
                ans.append((x,y))
            # print(x,y,v)
        for i in range(1,n):
            if i not in vis and 0 not in vis:
                ans.append((i,0))
                vis.add(i)
                vis.add(0)
                break
        # for i in range(n):
        #     print(i, bin(i)[2:])
        # print()
        # for i,j in ans:
        #     print(i,j)

        if len(vis) != n:
            print(-1)
        else:
            for i,j in ans:
                print(i,j)
        continue

    for num in range(n):
        for j in range(17):
            if (1<<j)&num:
                bit_d[j].append(num)
    # print(bit_d)
    ok = True
    ans = []
    vis = set()
    s = 0
    for b in range(17,-1,-1):
        if (1<<b)&k :
            if len(bit_d[b]) < 2 :
                ok = False
            else:
                x = bit_d[b].popleft()
                y = bit_d[b].popleft()
                ans.append((x,y))
                vis.add(x)
                vis.add(y)
                s+= x&y
            # find two elements with 

    for i in range(1,n):
        if i not in vis:
            ans.append((i,0))
            vis.add(0)
            vis.add(i)
            break

    if len(vis) != n or s != k:
        print(-1)
    else:
        # print(s)
        [print(*i) for i in ans]
    # print(ans,ok,vis)




            



