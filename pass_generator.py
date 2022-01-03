import random
import string


def pass_gen(count: int = 10, with_punctuation=False) -> str:
    str_out = ""
    nums = [n for n in range(count)]
    random_symbols = [random.choice(string.ascii_lowercase) for _ in range(count)]
    random_symbols.extend(nums)
    if with_punctuation:
        random_symbols.extend(random.choice(string.punctuation) for _ in range(int(count//2)))
    print(random_symbols)

    for i in range(count):
        str_out+= str(random.choice(random_symbols))
    return str_out


print(pass_gen(100, with_punctuation=True))

