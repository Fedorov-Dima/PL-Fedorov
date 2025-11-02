lst = []
flag = False

# Создаем кортеж
# Заполняем список значениями
for i in range(5):
    num = float(input("Введите число: "))
    if int(num) != float(num):
        flag = True
    lst.append(num)

# Делаем кортеж
tup = tuple(lst)

# Выводим кортеж
if flag:
    print(tup)
else:
    tup = tuple(sorted(tup))
    print(tup)