import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


arr = [1, 2, 1]
for mx in range(3, 11):
    arr.append(mx)
    arr.extend(arr[:len(arr) - 1])

for _ in range(*maps()):
    n, = maps()
    print(*arr[:n])
