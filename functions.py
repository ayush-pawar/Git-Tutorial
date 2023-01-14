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


def skyline(word):
    skylined_word = ""

    for position in range(len(word)):
        if position % 2 != 0:
            upper_case_letter = word[position].upper()
            skylined_word += upper_case_letter
        else:
            lower_case_letter = word[position].lower()
            skylined_word += lower_case_letter

    return skylined_word


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a <= b:
            return a
        else:
            return b
    else:
        if a >= b:
            return a
        else:
            return b


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def pattern(n):
    row = 1
    while row <= n:
        col = 1
        print_val = row

        while col <= row:
            print(print_val, end=" ")
            print_val += 1
            col += 1

        print("\n")
        row += 1


pattern(5)
