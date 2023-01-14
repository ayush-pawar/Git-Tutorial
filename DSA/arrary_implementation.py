def contains_duplicate(nums):
    unique_nums = []

    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    print(f"Unique Nums: {unique_nums}")
    print(f"Nums: {nums}")

    return len(nums) == len(unique_nums)


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
