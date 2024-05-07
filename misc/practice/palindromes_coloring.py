import sys

def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    n, k = map(int, input().split())
    s = input()
    # if n == k :
    # 	print(1)
    freq, a = [0] * 26, ord("a")
    for i in s:
        freq[ord(i) - a] += 1
    tote = toto = 0
    for i in range(26):
        if freq[i] % 2:
            x = freq[i] - 1
            toto += 1
            tote += x
        else:
            tote += freq[i]
    # print(tote, toto)
    ans = tote // k
    toto += tote - (ans * k)

    if ans % 2 == 0 and toto >= k:
        ans += 1
    # print(ans, tote,toto ,k)
    print(max(1, ans))


tc = int(input())
while tc:
    tc -= 1
    main()
