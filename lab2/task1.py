list1 = list(map(int, input("Введите числа первого списка через пробел: ").split()))
list2 = list(map(int, input("Введите числа второго списка через пробел: ").split()))

intersection = sorted(set(list1) & set(list2))

print("Числа, входящие в оба списка:", intersection)