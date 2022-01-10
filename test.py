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
# print(is_pangram(pangram), True)
# print(is_pangram_2(pangram), True)
n = 5
max_row = [(n + 1) if (n + 1) % 2 != 0 else None for n in range(n)]


def row_sum_odd_numbers(n):
    num_count = 0
    for i in range(n):
        num_count += (i + 1) * 2
    # print('all nums: ', num_count)

    max_row = [n + 1 if (n + 1) % 2 != 0 else None for n in range(num_count)]
    # print(max_row)
    odd_nums_list = list(filter(lambda x: x is not None, max_row))
    # print(odd_nums_list)
    list_rows = []
    for row in range(n):
        list_rows.append(odd_nums_list[:row + 1])
        odd_nums_list = odd_nums_list[row + 1:]
    # print(list_rows)
    sum = 0
    for num in list_rows[-1]:
        sum += num
    return sum


# print(row_sum_odd_numbers(41))

def anagrams(word, words):
    word_sorted_letters = list(word)
    word_sorted_letters = sorted(word)
    # print("the word's letters are", word_sorted_letters)
    list_out = []
    for word_from_words in words:

        sorted_letters = sorted(list(word_from_words))
        if sorted_letters == word_sorted_letters:
            list_out.append(word_from_words)
    return list_out


# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])


def find_it(seq):
    num_count_dict = {}
    for n in range(len(seq)):
        item = seq[n]
        if num_count_dict.get(item, None):  # if i have already have this key in dict
            num_count_dict[item] += 1
        else:  # if the key is new for the dict
            num_count_dict[item] = 1
    for (k, v) in num_count_dict.items():
        if v % 2 != 0:
            return k


find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])


def num_uni(default_num, input_sign_num):
    if input_sign_num is None:
        return default_num
    else:
        input_sign_num = input_sign_num.split()
        if input_sign_num[0] == '+':
            return default_num + int(input_sign_num[1])
        elif input_sign_num[0] == "-":
            return default_num - int(input_sign_num[1])
        elif input_sign_num[0] == "*":
            return default_num * int(input_sign_num[1])
        elif input_sign_num[0] == "//":
            return default_num / int(input_sign_num[1])
        return input_sign_num


def zero(n=None):
    return num_uni(0, n)


def one(n=None):
    return num_uni(1, n)


def two(n=None):
    return num_uni(2, n)


def three(n=None):
    return num_uni(3, n)


def four(n=None):
    return num_uni(4, n)


def five(n=None):
    return num_uni(5, n)


def six(n=None):
    return num_uni(6, n)


def seven(n=None):
    return num_uni(7, n)


def eight(n=None):
    return num_uni(8, n)


def nine(n=None):
    return num_uni(9, n)


def plus(num=None):
    if not num is None:
        return f"+ {num}"


def minus(num=None):
    if not num is None:
        return f"- {num}"


def times(num=None):
    if not num is None:
        return f"* {num}"


def divided_by(num=None):
    if not num is None:
        return f"/ {num}"


def fabonacci(n):
    pass


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


factorial(20)


# print(factorial(18))
# print(factorial(19))
# print(factorial(20))
# print(factorial(15))
# print(factorial(10))


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# print(comp(a1, a2), True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# print(comp(a1, 2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# print(comp(a1, a2), False)
a1 = [2, 2, 3]
a2 = [4, 9, 9]


# print(comp(a1, a2), False)

#
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
#
# Concatenate the consecutive strings of strarr by 2, we get:
#
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
#
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so
# longest_consec(strarr, 2) should return "folingtrashy".
#
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

def longest_consec(strarr, k):
    if len(strarr) == 0 or k < 0 or k > len(strarr) :
        return ''
    new_list = []
    for i in range(len(strarr)):
        str_conc = ''

        for i_conc in range(k):
            if len(strarr) > (i + i_conc):
                str_conc += strarr[i + i_conc]
        new_list.append(str_conc)

    new_list = sorted(new_list, key=lambda x: len(x), reverse=True)

    return new_list[0]


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1),
      "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3), "")
print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2),
      "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
print(longest_consec(['hlffffsssa', 'xxvvvvoo', 'bbbbbyynqqq', 'tttttpppyyzzz', 'iihhkkkddeeejjj', 'bbbmmkkkkkklljmmmuhhh', 'nnqqyyqqq', 'aaazzwrrii', 'bblaa', 'szzzuaxxxhr', 'qqssst', 'llwwwmmmzzzrppibbb', 'qqqirii', 'sssiooo', 'prpppccc', 'xxeeerssjddeee', 'tkdzvbbb', 'hhhaaauzzm', 'vfdddnn', 'dmggi', 'nsssxxweejwww', 'dqqggghafccc', 'kkvxx', 'hhhnsjjmm', 'mmllmmhn', 'ccqqzzcc', 'zzzqqkkkvvv', 'suuupppiffhh', 'ueuuubbbis', 'dddrrrcccmmmccc', 'fffoppdddaarr', 'dyyfqqq', 'zwwwiipiiixx', 'wwwjjqqqwwwww', 'llddqq', 'jjjuiiqqq', 'oqqxxxccrr', 'ooovvvrr', 'qqssxynn', 'hhhgggukkrhh', 'nnnppkkknbbpp', 'yyyllhhppphhq', 'ddfssseeeooejj', 'aaawwwwwzfffvzzz', 'cjlllllljjcccttdd', 'ddddzzz', 'oottccc', 'aabddvvv', 'rrrjr', 'gggcsscqqqjjjqq', 'dggkk', 'kkgggiuaauuf', 'nssslllqxxx', 'llqhhhbpppll', 'bhhhgggrrwss', 'ffwwwhhoobbib', 'ffttts', 'aadddaaaxh', 'uuuccgggr', 'unngg', 'yzzqqq', 'mmrrkkttjj', 'lllzzdnnnqqq', 'whbbfffyyaaa', 'iiiqeeeuuqqq', 'lllfftt', 'rrrddddddnnlll', 'hhhppuutrrrttt', 'kfsshhhattb', 'esssfqqiinnity', 'iidddeeewoo', 'ufffayyyc', 'ycccqqrfff', 'lewwggpppqkk', 'ddmggdeet', 'kkffxxkkkcqqvvv', 'nnnhhuuunn', 'yyykkmmrncxdddcc', 'rroodvh', 'wwkkkdaaarrr', 'dddxrxxx', 'pptttdfj', 'qqqpppimmm', 'aaayybbwbbddmm', 'kkkkkrr', 'bbiiinnnhhxxxbd', 'mrrrqq', 'xppxxxwwcguwv', 'jsseewwweee', 'ddxxxvvvvvggk', 'cmmmyydddqqquiiik', 'siifffdddrrrqqq', 'fffcciiioo', 'vvvbbjmcmmmjl', 'ggbbpppr', 'bbrrrhhllbqqq', 'keejjjeeett', 'kkkuuuhhhvvvooto', 'weeehhv', 'zzzjjjvvyzzz', 'fffnnnjjjw', 'appstttttt', 'kkaaaxyu', 'siioonnnnnn', 'dwwwnnnffrrzzznnnj', 'tfftthhlll', 'ssvvvhddoffo', 'fffhooocsssqb', 'sssggcccx', 'nnnjvvvhuuo', 'ppprrhfffapbbt', 'hhhoiyyyxxx', 'yyyfffpll', 'vvgaaauuu', 'uummmvn', 'uuxxxriiijk', 'eeehhhxcccoooll', 'aoooeffyyy', 'ttwffpp', 'ooorrrnwwuujjjjj', 'ppvvvfffeennggfbb', 'xxbbbcccvvhhhmmmtnnn', 'wyyfffjj', 'mmmfffxxuccsss', 'qqqhyycdd', 'ssiiioz', 'tttlllbbbkkkb', 'mmmdhsssddd', 'xxxtttiqqq', 'dddkfffqqzzzdd', 'aqqqfvv', 'zzzmyybb', 'fftuuurwzff', 'hxxxddlllkk', 'vvvvvjj', 'sssgggss', 'cnnppffyyrrvv', 'xkkkpppgt', 'njjssvvvvy', 'dddtttkkf', 'yyyooojjdkk'], 124))
