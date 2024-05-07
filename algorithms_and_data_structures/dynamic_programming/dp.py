import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
nCr, ceil = (
    lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r),
    lambda n, x: (n + x - 1) // x,
)
osi, oso = (
    "/home/priyanshu/Documents/sublimetextproject/input.txt",
    "/home/priyanshu/Documents/sublimetextproject/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")
input = sys.stdin.readline
# def max_subarray_sum():b
# 	n, k, ans  =  I() , I() , -maxx
# 	ls , dp  = [0] + lint() , [[0 for i in range(k+1)] for _ in range(n+1)]
# 	for i in range(1, n +1):
# 		for  j in range(k + 1):
# 			dp[i][j] = max(ls[i], dp[i-1][j] + ls[i])
# 			if j :
# 				dp[i][j] = max(dp[i][j],  dp[i-1][j-1] - ls[i]) #i-1 ,j-1 because dp[i] be ls[i] already added hai
# 			ans = max(ans , dp[i][j])
# 	print(ans)


def ConvertRecur(str1, str2, m, n):
    # Convert str1 to str2 by replacing , deleting or inserting characters [Recursively]
    if n == 0:
        return m
    if m == 0:
        return n
    if str1[m - 1] == str2[n - 1]:
        return ConvertStr1ToStr2(str1, str2, m - 1, n - 1)
    return 1 + min(
        ConvertStr1ToStr2(str1, str2, m, n - 1),
        ConvertStr1ToStr2(str1, str2, m - 1, n),
        ConvertStr1ToStr2(str1, str2, m - 1, n - 1),
    )
    # Time Complexity - O(3^m)


def ConvertDp(str1, str2, n, m):
    # Convert str1 to str2 by replacing , deleting or inserting characters
    dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]
                )  # Delete , Replace , Insert
    return dp[n][m]
    # Time Complexity - O(n*m)
    # Space Complexity - O(n*m)


def ConvertTopDownRecursiveDp(str1, str2, n, m, dp):
    if n == 0:
        return m
    if m == 0:
        return n
    if dp[n][m] != -1:
        return dp[n][m]
    if str1[n - 1] == str2[m - 1]:
        dp[n][m] = (
            ConvertTopDownRecursiveDp(str1, str2, n - 1, m - 1, dp)
            if dp[n - 1][m - 1] == -1
            else dp[n - 1][m - 1]
        )
        return dp[n][m]
    else:
        if dp[n - 1][m - 1] == -1:
            dp[n - 1][m - 1] = ConvertTopDownRecursiveDp(str1, str2, n - 1, m - 1, dp)
        if dp[n - 1][m] == -1:
            dp[n - 1][m] = ConvertTopDownRecursiveDp(str1, str2, n - 1, m, dp)
        if dp[n][m - 1] == -1:
            dp[n][m - 1] = ConvertTopDownRecursiveDp(str1, str2, n, m - 1, dp)
        dp[n][m] = 1 + min(dp[n - 1][m - 1], dp[n - 1][m], dp[n][m - 1])
        return dp[n][m]
    # Time Complexity - O(n*m)
    # Space Complexity - O(n*m)


# str1 = 'sunday'	; str2 = 'saturday' ; n = len(str1) ; m = len(str2)
# dp = [[-1 for i in range(m+1)] for i in range(n+1)]
# print(ConvertTopDownRecursiveDp(str1, str2, len(str1) , len(str2) , dp))


def m_cost(n, m, arr):
    dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    dp[0][0] = arr[0][0]
    for i in range(1, n + 1):
        dp[i][0] = arr[i][0] + dp[i - 1][0]
    for i in range(1, m + 1):
        dp[0][i] = arr[0][i] + dp[0][i - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    return dp[n][m]
    # Basically , base case if prefix of first row and column
    # Time Complexity - O(n*m)
    # Space Complexity - O(n*m)


def coinchange(arr, m, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(m):
        for j in range(arr[i], n + 1):
            dp[j] += dp[j - arr[i]]
    return dp[n]
    # Time Complexity - O(m*n)
    # Space Complexity - O(n)
    # dp[0] = 1 , becuase element - first index = 0

    # arr =[1, 2 , 3] ; m = len(arr) ; n = 4
    # print(coinchange(arr, m, n))


# number of paths from top -left to right bottom
# the number of paths to reach (n,m) = the number of paths which reaches (m , n-1 ) + the number of paths which reaches (n-1,m)
# Time Complexity - O(2^max(n,m)) (Recursive ) , O(n*m) (iterative )
# Space Complexity - O(1) (Recursive) , O(n*m) (Iterative)
n, m = 3, 3
dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
dp[1][1] = 1


def TopDown(x, y):
    if x == 1 or y == 1:
        dp[x][y] = 1
        return dp[x][y]
    dp[x - 1][y], dp[x][y - 1] = (
        TopDown(x - 1, y) if not dp[x - 1][y] else dp[x - 1][y]
    ), (TopDown(x, y - 1) if not dp[x][y - 1] else dp[x][y - 1])
    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
    return dp[x][y]


def BottomUp(x, y):
    for i in range(n):
        dp[i][0] = 1
    for i in range(m):
        dp[0][i] = 1
    for i in range(1, x):
        for j in range(1, y):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[x - 1][y - 1]


# print(BottomUp(n , m)) ; print(*dp , sep='\n')
# print(TopDown(3, 3)) ; print(*dp , sep='\n')
# There's also a Combinatorial approach , where Dest(1 ,1) for is nCr(max(n,m), min(n,m))
