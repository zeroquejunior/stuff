list = [1, 1, 6, 6, 6, 6, 9, 1, 1]


def sum_69(list):
    add = True

    summed = 0

    for i in list:
        if add:
            if i != 7:
                summed += i
            else:
                add = False
        else:
            if i == 9:
                add = True

    return float(summed)


def rola():
    return sum_69(list) + 99


def divide():
    return round(rola() / 30, 5)


def test_results_sum69():
    print("@" * 60)
    print(f"Teste sum69 {sum_69(list) == 4} ")
    print(f"Teste divide {float(divide()) == 3.43333} ")
    print("@" * 60)


test_results_sum69()
print(divide())
