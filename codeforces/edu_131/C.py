from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # d = defaultdict(list)
    # available = set()
    # for idx,i in enumerate(a):
    #     d[i].append(idx)

    # for i in range(1, n + 1):
    #     if i in d:
    #         continue
    #     available.add(i)

    # occ = [False]*n
    # ans = 0
    # while m:
    #   add_ = set()
    #   for i in d :
    #       if len(d[i]):
    #           d[i].pop()
    #           if not len(d[i]):
    #               add_.add(i)
    #           m-=1
    #   cnt = len(available)
    #   for i in d:
    #       while cnt > 0 and len(d[i]) > 0 :
    #           d[i].pop()
    #           cnt-=1
    # d = defaultdict(int)
    # for i in a:
    #     d[i] += 1
    # time = 0
    # nn = m
    # # free = []
    # free = n - len(d)
    # # next_free = set()
    # cnt = 0
    # for i in range(1, n + 1):
    #     if i not in d:
    #         free.append(i)

    # while m > 0:
    #     p = 0
    #     # break
    #     for i in d:
    #         if d[i] == 0:
    #             continue
    #         elif d[i] == 1:
    #             d[i] -= 1
    #             free.add(i)  # free for next iteration
    #             m -= 1
    #             p = max(p, 1)
    #         else:
    #             d[i] -= 2
    #             m -= 2
    #             next_free.add(i)
    #             p = max(p, 2)
    #             if len(free) > d[i]:
    #                 x = d[i]
    #             else:
    #                 x = len(free)
    #             d[i] -= x
    #             m -= x

    #     cnt += 1
    #     if cnt % 2 == 0:
    #         for i in next_free:
    #             free.add(i)

    #     time += p

    # unemployed = n - len(d)
    # next_free = []

    # while m > 0 :
    #     for i in d :
    #         if d[i] == 0 :
    #             continue
    #         if d[i] == 1 :
    #             d[i] -= 1
    #             m -=  1
    #             next_free.append((i,cnt+2))
    #         else:
    #             d[i] -= 2
    #             m-=2
    #             if d[i] > 0 :
    #                 if free:
    #                     free-=1
    #                     m-=1
    #                     next_free.append((i,cnt+2))

    # print(time)

    # if any tasks are left to be assigned
    # arr = [[i, d[i]] for i in range(1, n + 1)]
    # free = n - len(d)
    # time = []
    # # print(arr)
    # arr.sort(key=lambda x: -x[1])
    # i = 0
    # will_be_free = []
    # cnt = 0
    # while i < n:
    #     while free > 0:
    #         worker, times = arr[i]
    #         if times == 1:
    #             time.append(1)
    #             i += 1
    #         elif times == 2:
    #             time.append(2)
    #             will_be_free.append((worker, cnt + 2))
    #             i += 1
    #         else:
    #             will_be_free.append((worker, cnt + 2))
    #             x = min(times, free)
    #             times -= x
    #             free -= x

    #             if times <= 0:
    #                 i += 1
    #                 time.append(2)
    #             else:
    #                 arr[i][1] = times
    #     cnt += 1
    #     for j, k in will_be_free:
    #         if k == cnt:
    #             free += 1
    # print(time)
    # dp = [[0 for _ in range(m)] for __ in range(2)]
    # d = defaultdict(int)
    # for i in a :
    #     d[i]+=1
    # for i in range(1, n + 1):
    #     if i not in d :
    #         dp[0][i-1] = 0

    # for i in range(m):

    #     # i am at task i
    #     # use free worker who is pro
    #         #
    #     # use other free worker not pro
    d = defaultdict(list)
    for idx, i in enumerate(a):
        d[i].append(idx)
    available = []
    for i in range(1, n + 1):
        if i not in d:
            available.append(i)

    h = []
    for i in range(1, n + 1):
        if i in d:
            x = (1, i, d[i].pop())
        else:
            p = available.pop()
            x = (2, i, p)
            available.append(p)
        heappush(h, x)
    ans = 0
    vis = [False] * (m + 1)
    free = [True] * (n + 1)

    while h:
        time, worker, task = heappop(h)
        if vis[task]:
            continue
        ans = max(ans, time)
        if a[task - 1] == worker:
            x = (
                time + 1,
                worker,
            )

    # while h:


"""






"""

############
