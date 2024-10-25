n = int(input('Длина массива: '))
a = []
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
print(max(a))
print(a[::-1])
