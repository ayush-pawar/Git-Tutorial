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


print(skyline('Anthropomorphism'))
