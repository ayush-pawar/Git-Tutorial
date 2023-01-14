def linear_search(numbers, target):
    """Returns index of the Target if found, else, returns None"""
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at Index: {index}")
    else:
        print("Target not found")


numbers = [1, 2, 3, 4]
target = 3

result = linear_search(numbers, target)
verify(result)
