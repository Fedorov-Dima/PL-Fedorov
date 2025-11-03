from functools import reduce

lst = []
for i in range(int(input("Длина списка: "))):
    lst.append(float(input("Введите число: ")))

positive_numbers = [i for i in lst if i >= 0]
negative_numbers = list(filter(lambda i: i < 0, lst))
print(lst)
print(positive_numbers)
print(negative_numbers)
print(sum(positive_numbers) / len(positive_numbers))
print(reduce(lambda x, y: x * y, negative_numbers) ** (1 / len(negative_numbers)))