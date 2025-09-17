from random import shuffle

def app() -> None:
    ...


def shuffle_words(text: str) -> str:
    words = text.split(' ')
    shuffle(words)
    return ' '.join(words)


def odd_word_chars_cnt(text: str) -> str:
    cnt = 0
    words = text.split(' ')
    for word in words:
        if len(word)%2==1:
            cnt += 1
    return cnt


def russian_threecolor(colors: list[str]) -> list[str]:
    for i in range(len(colors)):
        match colors[i]:
            case "белый":
                colors[0], colors[i] = colors[i], colors[0]
            case "синий":
                colors[1], colors[i] = colors[i], colors[1]
            case "красный":
                colors[2], colors[i] = colors[i], colors[2]
    return colors


