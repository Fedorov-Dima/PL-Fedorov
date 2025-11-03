from random import randint

# последовательность целых чисел
lst = [randint(1, 10) for i in range(20)]
lst[-1] = 0 # Оканчивается нулем

s = 0
i = 0
while True:
    s += lst[i]
    i += 1
    if lst[i] == 0:
        break
print("sum:", s)
print("count:", i)