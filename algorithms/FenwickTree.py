

def get_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


def get_sum_segment(s, t):
    ans = get_sum(t) - get_sum(s - 1)
    return ans


def add(i, x):  # index , value
    while i <= n:
        tree[i] += x  # updating all the positions in the tree which are responsible for this index
        i += i & -i
