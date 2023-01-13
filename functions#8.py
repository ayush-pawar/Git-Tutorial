def my_func(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum


print(my_func(1, 2, 3))
