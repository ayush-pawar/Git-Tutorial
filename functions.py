def get_sum(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum


def pick_evens(*args):
    even_nums = []

    for arg in args:
        if arg % 2 == 0:
            even_nums.append(arg)

    return even_nums
