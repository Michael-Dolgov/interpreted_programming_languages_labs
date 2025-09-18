from string import ascii_lowercase


RUSSIAN_SYMBOLS = "йцукенгшщзхъфывапролджэёячсмитьбю"


def russian_symbols_cnt(text: str) -> int:
    cnt = 0
    for symbol in text:
        if symbol in RUSSIAN_SYMBOLS:
            cnt += 1
    return cnt


def latin_symbols_cnt(text: str) -> int:
    cnt = 0
    for symbol in text:
        if symbol in ascii_lowercase:
            cnt += 1
    return cnt


def max_int_in_string(text: str) -> int:
    data = text.split(' ')
    maximum = None
    for datapiece in data:
        if '.' not in datapiece and datapiece.isdigit():
            num = int(datapiece)
            if maximum == None:
                maximum = num
            elif maximum < num:
                maximum = num
    return maximum


def min_int_in_string(text: str) -> int:
    data = text.split(' ')
    minimum = None
    for datapiece in data:
        if '.' not in datapiece and datapiece.isdigit():
            num = int(datapiece)
            if minimum == None:
                minimum = num
            elif minimum > num:
                minimum = num
    return minimum
