def partition(nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low


nums = [4, 7, 1, 2, 1]
l = 0
r = 4
x = partition(nums, l, r)
print(x)
print(nums)
