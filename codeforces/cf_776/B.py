def all_p(l, r, a):
    ans = 0
    for i in range(l, r + 1):
        ans = max(ans, i // a + (i % a))
    # if ans == 410:
    #     print(i)
    #     break
    return ans


for _ in range(int(input())):
    l, r, a = map(int, input().split())
    d = r // a
    k = (r // a) + (r % a)
    f = r - (r % a + 1)
    if f >= l and f <= r:
        k = max(f // a + (f % a), k)
    k = max(l // a + (l % a), k)
    print(k)
