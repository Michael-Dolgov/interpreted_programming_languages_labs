MESSAGE = "Введите строку: "
inputs = []

while True:
    text = input(MESSAGE)
    if not text:
        break
    inputs.append(text)

inputs.sort(key=len, reverse=True)

print(inputs)