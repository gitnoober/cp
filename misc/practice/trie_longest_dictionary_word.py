import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
osi, oso = (
    "/home/priyanshu/Documents/cp/input.txt",
    "/home/priyanshu/Documents/cp/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


# think about the edge cases


def dfs(node, so_far, temp, nxt, is_terminal):
    if len(so_far) > len(temp[-1]):
        temp.append(so_far)
    for c in range(26):
        tmp = nxt[node][c]
        if tmp and is_terminal[tmp]:
            dfs(tmp, so_far + chr(c + 97), temp, nxt, is_terminal)


def main():
    a = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    N = 1
    nxt = [[0] * 26]
    is_terminal = [False]
    for i in a:
        node = 0
        for c in i:
            if nxt[node][ord(c) - 97] == 0:
                nxt[node][ord(c) - 97] = N
                N += 1
                nxt.append([0] * 26)
                is_terminal.append(False)
            node = nxt[node][ord(c) - 97]
        is_terminal[node] = True
    temp = [""]
    dfs(0, "", temp, nxt, is_terminal)
    print(temp[-1])


main()
