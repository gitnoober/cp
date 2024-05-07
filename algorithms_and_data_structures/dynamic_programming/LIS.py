def LongestIncreasingSubsequence(arr):
    n = len(arr)
    L = [0] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
    return print(L, max(L))
    # Time Complexity -  O(n^2)
    # Space Complexity - O(n)
