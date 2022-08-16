N = int(input())
for _ in range(N):
    s = input()
    k = 10 ** (len(s) - 1)
    print(int(s) - int(k))
