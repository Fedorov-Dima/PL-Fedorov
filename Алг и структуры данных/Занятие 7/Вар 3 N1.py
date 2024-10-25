n = int(input('Длина массива: '))
a = []
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
s = sum(a[1::2])
print(a)
print(s)
