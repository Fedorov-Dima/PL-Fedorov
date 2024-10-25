n = int(input('Длина массива: '))
a = []
b = []
print('Вводите числа')
for i in range(n):
    x = int(input())
    a.append(x)
    if x != 0:
        b.append(x)
b = sum(b) / len(b)
for i in range(n):
    if a[i] == 0:
        a[i] = b
print(a)
