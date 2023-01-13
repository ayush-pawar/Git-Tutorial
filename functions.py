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


print(lesser_of_two_evens(2, 5))
