MESSAGE = "Введите строку: "
inputs = []

while True:
    text = input(MESSAGE)
    if not text:
        break
    inputs.append(text)

inputs.sort(key=lambda s: len(s.split()))

print(inputs)