def binary_search(nums, target):
    # O(log n)
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


nums = [-1, 3, 4, 6, 8, 42, 45]
