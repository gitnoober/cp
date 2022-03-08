"""
Linear Memory i.e n length array can have upto 4*n vertices
"""

"""
Generic Implementation
"""


class SegmentTree:
    def __init__(self, arr, func=max):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * 4 * self.n
        self._func = func

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)
            self.tree[v] = self._func(self.tree[v * 2], self.tree[v * 2 + 1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        elif l == tl and r == tr:
            return self.tree[v]
        else:
            tm = (tl + tr) // 2
            return self._func(
                self.query(v * 2, tl, tm, l, min(r, tm)),
                self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), tr),
            )

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, new_val)

            self.tree[v] = self._func(self.tree[v * 2], self.tree[v * 2 + 1])


"""
Counting the number of zeroes, searching for the k-th zero using segment tree.
Build will remain the same(slight changes in the base case , like count will increase if it's a zero) just use this function to query
"""


def kth_zero(self, v, tl, tr, k):
    if k > self.tree[v]:
        return -1
    if tl == tr:
        return self.tree[v]
    tm = (tl + tr) // 2
    if self.tree[v] >= k:
        return self.kth_zero(v * 2, tl, tm, k)
    else:
        return self.kth_zero(v * 2 + 1, tm + 1, tr, k - self.tree[v * 2])


a = [5, 4, 3, 2]
t = [0] * len(a) * 4


def build(a, v, tl, tr):
    if tl == tr:
        t[v] = a[tl]
    else:
        tm = (tl + tr) // 2
        build(a, v * 2, tl, tm)
        build(a, v * 2 + 1, tm + 1, tr)
        t[v] = 0


build(a, 0, 0, len(a) - 1)
print(t)
