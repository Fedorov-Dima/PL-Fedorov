from random import randint

def func():
    tup = tuple([randint(0, 10) for i in range(20)]) # Кортеж из 20 случайных значений
    elem = randint(0, 10) # Случайный элемент
    print(f"Исходный кортеж: {tup}")
    print(f"Случайный элемент: {elem}")

    try:
        id1 = tup.index(elem)
    except ValueError:
        return ()

    try:
        id2 = tup.index(elem, id1 + 1)
    except ValueError:
        return tup[id1:]

    return tup[id1:id2 + 1]

print("Результат:", func())