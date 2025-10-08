# 3 -> 3, 15, 27, 39, 51
def task3(arr: list[int], idx: int) -> bool:
    return arr[idx] == max(arr)


def task15(arr: list[int], idx: int) -> bool:
    if idx == 0 or idx == len(arr) - 1:
        return False
    return arr[idx] < arr[idx - 1] and arr[idx] < arr[idx + 1]


def task27(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    return arr[1:] + arr[:1]


def task39(arr: list[int]) -> list[int]:
    return arr[::2] + arr[1::2]


def task51(arr: list[int]) -> tuple[list[int], list[int]]:
    L1 = []
    L2 = []
    for x in arr:
        if x not in L1:
            L1.append(x)
            L2.append(arr.count(x))
    return L1, L2


def main():
    print("Выберите задачу: 3, 15, 27, 39, 51")
    choice = int(input("Введите номер задачи: "))

    if choice == 3:
        arr = list(map(int, input("Введите массив через пробел: ").split()))
        idx = int(input("Введите индекс: "))
        print(task3(arr, idx))

    elif choice == 15:
        arr = list(map(int, input("Введите массив через пробел: ").split()))
        idx = int(input("Введите индекс: "))
        print(task15(arr, idx))

    elif choice == 27:
        arr = list(map(int, input("Введите массив через пробел: ").split()))
        print(task27(arr))

    elif choice == 39:
        arr = list(map(int, input("Введите массив через пробел: ").split()))
        print(task39(arr))

    elif choice == 51:
        arr = list(map(int, input("Введите массив через пробел: ").split()))
        L1, L2 = task51(arr)
        print("L1 =", L1)
        print("L2 =", L2)

    else:
        print("Нет такой задачи")


if __name__ == '__main__':
    main()