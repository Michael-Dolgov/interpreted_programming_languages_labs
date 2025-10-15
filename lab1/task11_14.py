import string
from collections import Counter


def sort_lines_by_char_freq_diff(text: str) -> list[str]:
    lines = text.splitlines()

    def diff_value(s: str) -> int:
        freq = {}
        for ch in s.lower():
            if ch.isalpha():
                freq[ch] = freq.get(ch, 0) + 1
        if not freq:
            return float("inf")
        char = max(freq, key=freq.get)
        freq_in_str = freq[char]
        pos = string.ascii_lowercase.index(char) + 1
        return abs(freq_in_str - pos)

    return sorted(lines, key=diff_value)


def sort_lines_by_squared_deviation(text: str) -> list[str]:
    lines = text.splitlines()
    alphabet = string.ascii_lowercase
    N = len(alphabet)
    uniform_freq = 1 / N

    def deviation(s: str) -> float:
        letters = [ch.lower() for ch in s if ch.isalpha()]
        if not letters:
            return float("inf")
        freq = {}
        for ch in letters:
            freq[ch] = freq.get(ch, 0) + 1
        most_freq_char = max(freq, key=freq.get)
        f_s = freq[most_freq_char] / len(letters)
        return (f_s - uniform_freq) ** 2

    return sorted(lines, key=deviation)


def sort_by_vc_cv_diff(text: str) -> list[str]:
    lines = text.splitlines()
    vowels = set("aeiouAEIOU")

    def vc_cv_diff(s: str) -> int:
        letters = [ch for ch in s if ch.isalpha()]
        vc = 0
        cv = 0
        for i in range(len(letters) - 1):
            if letters[i] in vowels and letters[i+1] not in vowels:
                vc += 1
            elif letters[i] not in vowels and letters[i+1] in vowels:
                cv += 1
        return vc - cv

    return sorted(lines, key=vc_cv_diff)


def sort_by_squared_div_char_freq(text: str) -> list[str]:
    lines = text.splitlines()
    if not lines:
        return []
    
    global_counter = Counter(text.replace("\n", ""))
    most_common_char, global_count = global_counter.most_common(1)[0]
    total_chars = sum(global_counter.values())
    
    global_freq = global_count / total_chars
    
    def squared_deviation(line: str) -> float:
        if not line:
            return global_freq**2
        count = line.count(most_common_char)
        freq = count / len(line)
        return (freq - global_freq) ** 2
    
    return sorted(lines, key=squared_deviation)


def app(choise: int) -> None:
    MESSAGE = "Введите текст: "
    match choise:
        #3
        case 11:
            sort_lines_by_char_freq_diff(input(f"{MESSAGE}"))
        #5
        case 12:
            sort_lines_by_squared_deviation(input(f"{MESSAGE}"))
        #7
        case 13:
            sort_by_vc_cv_diff(input(f"{MESSAGE}"))
        #12
        case 14:
            sort_by_squared_div_char_freq(input(f"{MESSAGE}"))


if __name__ == '__main__':
    userChoise = int(input("Выберите задачу 11-14: "))
    app(userChoise)
