import string

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



def app():
    choise = int(input("Выберите задачу 11-14: "))
    match choise:
        #3
        case 11:
            sort_lines_by_char_freq_diff(input("Введите текст: "))
        #5
        case 12:
            pass
        #7
        case 13:
            pass
        #12
        case 14:
            pass

if __name__ == '__main__':
    app()
