import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


n, s = maps()
if n == 1:
    if s == 1 and s == 1:
        print("NO")
    else:
        print("YES", s, s - 1, sep="\n")
    exit()

if s >= n * 2:
    print("YES")
    print("2 " * (n - 1), s - 2 * (n - 1), sep="")
    print(1)
    exit()

else:
    print("NO")
    exit()

# x = s - (n-2)

# if x % 2:
# 	m1 = x//2
# 	m2 = x//2 + 1
# else:
# 	m1 = m2 = x//2


# arr = [1]*n
# arr[0] = m1
# arr[1] = m2
# k = (n-2) + 1


# sum_ = 0
# i = 0
# ok = False
# sum_2 = s
# if sum_ == k or s-k == sum_:
# 	ok = True

# while i < n:
# 	sum_+=arr[i]
# 	sum_2 -= arr[i]
# 	if sum_ == k or sum_ == s-k or sum_2 == k or sum_2 == s- k:
# 		ok = True
# 	if sum_ > k:
# 		sum_-=arr[i]
# 	i+=1


# if ok:
# 	print('NO')

# else:

# 	print('YES')
# 	print(*arr)
# 	print(k)
