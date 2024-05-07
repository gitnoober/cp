def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def merge_array(arr1, arr2):
    arr = []
    i, j = 0, 0
    n1 = len(arr1)
    n2 = len(arr2)
    while len(arr) < n1 + n2:
        while (
            i < n1 and j < n2 and arr1[i] < arr2[j]
        ):  # [3, 5 ,4 ] -- [2 , 2 , 3] -- 3 < 2
            arr.append(arr1[i])
            i += 1
        while j < n2 and i < n1 and arr2[j] < arr1[i]:
            arr.append(arr2[j])
            j += 1

        while i < n1:
            arr.append(arr1[i])
            i += 1

        while j < n2:
            arr.append(arr1[j])
            j += 1
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        n1, n2, i, j, k = len(L), len(R), 0, 0, 0
        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            k += 1
            i += 1

        while j < n2:
            arr[k] = R[j]
            k += 1
            j += 1
