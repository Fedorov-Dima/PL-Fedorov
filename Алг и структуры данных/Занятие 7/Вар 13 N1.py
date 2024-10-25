a = []
n = int(input('Длина масива '))
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if a.count(a[i]) > 1:
        print(a[i], i)
