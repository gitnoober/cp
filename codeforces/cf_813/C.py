from collections import defaultdict


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for i in range(self.n + 1)]

    def get_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def get_sum_segment(self, s, t):
        return self.get_sum(t) - self.get_sum(s - 1)

    def add(self, i, x):  # index , value
        while i <= self.n:
            # updating all the positions in the tree which are responsible for this index
            self.tree[i] += x
            i += i & -i


N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    tree = FenwickTree(n + 1)
    idx = None
    for i in range(n - 1, -1, -1):
        x = tree.get_sum(a[i] - 1)
        if x > 0:
            idx = i
            break
        tree.add(a[i], 1)
    # print(idx)
    if idx is None:
        print(0)
        continue
    # zero = [-1]*n
    d = defaultdict(list)
    for i in range(n):
        d[a[i]].append(i)

    mx = 0
    for j in range(idx + 1):
        for x in d[a[j]]:
            mx = max(mx, x)
    # print(mx)
    se = set()
    for i in range(mx + 1):
        se.add(a[i])
    print(len(se))
