a = []
n = int(input('Длина масива '))
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
print(a)
a[a.index(min(a))], a[a.index(max(a))] = a[a.index(max(a))], a[a.index(min(a))]
print(a)
