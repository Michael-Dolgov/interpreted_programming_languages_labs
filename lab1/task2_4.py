from random import shuffle

def app() -> None:
    ...


def shuffle_words(text: str) -> str:
    words = text.split(' ')
    shuffle(words)
    return ' '.join(words)


