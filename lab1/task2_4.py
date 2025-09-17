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


