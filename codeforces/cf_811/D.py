# lOOKOUT FOR THE EDGE CASES


def cmp(d, s2, red):
    mx = 0
    st = None
    for idx in d[s2]:
        i = idx
        l = idx + len(s2)
        cnt = 0
        while i < l:
            if red[i] == 0:
                cnt += 1
            i += 1
        if cnt > mx:
            mx = cnt
            st = idx
    return mx, st


def sol():
    def make_it_red(start, end):
        for i in range(start, end):
            red[i] = 1

    def check(red):
        for i in red:
            if i == 0:
                return False
        return True

    t = input()
    n = int(input())
    inp = {input(): _ + 1 for _ in range(n)}

    all_s, N, d = set(), len(t), defaultdict(list)
    for i in range(N):
        for j in range(i + 1, N + 1):
            x = t[i:j]
            if x in inp:
                d[x].append(i)
                all_s.add(x)

    red, ans, farr, tl = (
        [0 for _ in range(len(t))],
        float("inf"),
        [],
        len(all_s),
    )
    ccc = 0
    for all_s in permutations(all_s, tl):
        ccc += 1
        red, moves, arr = [0 for _ in range(N)], 0, []
        for _ in range(len(t)):
            mx, st, end, sss = 0, None, None, None
            for string in all_s:
                x, y = cmp(d, string, red)
                if x > mx:
                    mx, st, end, sss = x, y, y + len(string), string
            if mx == 0:
                break
            make_it_red(st, end)
            arr.append((inp[sss], st + 1))
            moves += 1

        if check(red) and moves < ans:
            ans = moves
            farr = arr

        if ccc >= (N // 2) + 50:
            break

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
        for i in farr:
            print(*i)


# tc = int(input())
# while tc:
#     sol()
#     tc -= 1

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict
from itertools import permutations


def main():
    tc = int(input())
    while tc:
        sol()
        tc -= 1


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
