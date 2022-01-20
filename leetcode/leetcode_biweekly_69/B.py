from collections import deque, defaultdict


def longestPalindrome(words):
    front = []
    back = deque()
    middle = []
    _len = 0
    d = defaultdict(int)
    for i in words:
        d[i] += 1

    for i in d:
        if i[::-1] in d:
            if i == i[::-1]:
                continue

            while d[i] > 0 and d[i[::-1]] > 0:
                front.append(i)
                back.appendleft(i[::-1])
                d[i] -= 1
                d[i[::-1]] -= 1
                _len += 4

    for i in d:
        if i == i[::-1]:
            while d[i] > 1:
                d[i] -= 2
                _len += 4

            if d[i] == 1:
                ok = True
    if ok:
        _len += 2

    # print(front, middle, back, _len)
    return _len + len(middle) * 2


words = ["nn", "nn", "hg", "gn", "nn", "hh", "gh", "nn", "nh", "nh"]
print(longestPalindrome(words))

#        cc cc cc
