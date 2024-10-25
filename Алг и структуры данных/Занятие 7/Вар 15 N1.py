a = []
n = int(input('Длина масива '))
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
b = []
for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)
print(b)
