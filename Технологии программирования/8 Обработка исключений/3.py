try:
    n = int(input("Введите кол-во человек: "))

    middle_names = {}
    for i in range(n):
        try:
            fio = input("Введите ФИО через пробел: ").split()

            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        except IndexError:
            continue

    print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
    print("В расчете участвовало человек:", n)

except ValueError as err:
    print(f"Ошибка {err}! Проверьте введенные значения!")
except IndexError as err:
    print(f"Ошибка {err}! Проверьте введенные значения!")