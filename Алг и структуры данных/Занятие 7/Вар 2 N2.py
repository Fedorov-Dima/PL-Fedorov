n = int(input('Длина массива: '))
a = []
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
b, c = [], []
for i in a:
    if i > 0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
