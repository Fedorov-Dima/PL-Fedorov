from random import randint

# последовательность целых чисел
lst = [randint(1, 10) for i in range(20)]
lst[-1] = 0 # Оканчивается нулем

# Решение здорового человека:
# print(sum(lst))
# print(len(lst))

# Решение курильщика:
s = 0
i = 0
while lst[i] != 0:
    s += lst[i]
    i += 1
print("sum:", s)
print("count:", i)