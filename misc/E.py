from heapq import heappop, heappush
import sys

n = int(input())
m = int(input())
taks = []
for _ in range(m):
    x = input().split()
    taks.append(x)
workers = ["W" + str(i) for i in range(1, n + 1)]
h = []
A = []
for _ in range(min(n, m)):
    if len(taks[_]) == 2:
        # machine task
        finished = 0
        heappush(h, (finished, taks[_][0], workers[_]))
        heappush(A, (finished, taks[_][0], workers[_]))
    else:
        finished = int(taks[_][2])
        heappush(h, (finished, taks[_][0], workers[_]))
        heappush(A, (finished, taks[_][0], workers[_]))

# print(h)
# while h:
#     x = heappop(h)
#     print(x)
i = min(n, m)

while h and i < m:
    x = heappop(h)
    if len(taks) == 3:
        finished = x[0] + int(taks[i][2])
        heappush(h, (finished, taks[i][0], x[2]))
        heappush(A, (finished, taks[i][0], x[2]))
    else:
        finished = x[0]
        heappush(h, (finished, taks[i][0], x[2]))
        heappush(A, (finished, taks[i][0], x[2]))
    i += 1
ans = []
while A:
    x = heappop(A)
    val = [x[2], x[1], x[0]]
    ans.append(val)
    # print(x)

ans.sort(key=lambda x: (x[-1], x[1]))
for i in range(len(ans)):
    for j in ans[i]:
        sys.stdout.write(str(j) + " ")

    if i == len(ans) - 1:
        continue
    sys.stdout.write("\n")


# heappush(h, "W10")
# heappush(h, "W1")
# heappush(h, "W4")
# print(heappop(h))

"""
3
4
T1 Machine
T2 Manual 5
T3 Machine
T4 Machine



3
4
T1 Machine
T2 Machine
T3 Machine
T4 Machine
"""
