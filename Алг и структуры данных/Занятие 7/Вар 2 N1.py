n = int(input('Длина массива: '))
a = []
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
print(min(a))
print(a.index(min(a)))
