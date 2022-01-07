import string


def alphabet_position(text):
    str_out = []
    text = text.lower()
    for sym in text:
        if sym in string.punctuation or sym == ' ' or sym.isdigit():
            continue
        str_out.append(str(string.ascii_lowercase.index(sym) + 1))
    return ' '.join(str_out)


from random import randint


#
# print(alphabet_position("The sunset sets at twelve o' clock."),
#       "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
# print(alphabet_position("The narwhal bacons at midnight."),
#       "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
#
# number_test = ""
# for item in range(10):
#     number_test += str(randint(1, 9))
# # print(alphabet_position(number_test), "")
#
#


def unique_in_order(iterable):
    list_out = []
    i = 0
    while i < len(iterable):
        if not list_out == [] and iterable[i] is list_out[-1]:
            pass
        else:
            list_out.append(iterable[i])
        i += 1
    return list_out


# print(unique_in_order('ACccC'), ['A', 'B', 'C', 'D', 'A', 'B'])


def to_jaden_case(string):
    ls = string.split()
    list_out = []
    for it in ls:
        list_out.append(string.capworsd)
    return ' '.join(list_out)


quote = "How can mirrors be real if our eyes aren't real"


# print(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
# print(to_jaden_case(quote), "Aren't Real")


def digital_root(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if not sum < 10:
        sum = digital_root(sum)
    # print(sum)
    return sum


# print(digital_root(942))


import string


def is_pangram(s):
    s = s.lower()
    alpha_list = [_ for _ in string.ascii_lowercase]
    for sym in s:
        if sym in alpha_list:
            alpha_list.remove(sym)

    if len(alpha_list) == 0:
        return True
    else:
        return False


import string


def is_pangram_2(s):
    l = set(string.ascii_lowercase)
    r = set(s.lower())
    return l <= r


pangram = "Th quick, brown fox jumps ovr th lazy dog!"
print(is_pangram(pangram), True)
print(is_pangram_2(pangram), True)
n = 5
max_row = [(n + 1) if (n + 1) % 2 != 0 else None for n in range(n)]


def row_sum_odd_numbers(n):
    num_count = 0
    for i in range(n):
        num_count += (i + 1) * 2
    print('all nums: ', num_count)

    max_row = [n + 1 if (n + 1) % 2 != 0 else None for n in range(num_count)]
    print(max_row)
    odd_nums = list(filter(lambda x: x is not None, max_row))
    print(odd_nums)
    list_rows = []
    for row in range(len(odd_nums)):
        list_rows.append(odd_nums[:row])


row_sum_odd_numbers(4)
