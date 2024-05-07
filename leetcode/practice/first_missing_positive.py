import os
import sys

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


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


# THINK ABOUT THE EDGE CASES ..........


def func(nums):
    nums.append(0)
    n = len(nums)
    nums = [i if i > 0 and i < n else 0 for i in nums]
    for i in range(n):
        nums[nums[i] % n] += n
    for i in range(n):
        if nums[i] // n == 0:
            return i
    return n


nums = [1, 2, 3, 4]
print(func(nums))
# Should have thought of this one , O(1) space meaning probably utilising the input array and usage of a hashmap is obvious
# the  diff. is the array is utilised as a hashmap and the clever way of increasing every value of a keys that are present in the array
# just leaving the smallest element with a 0 value .
