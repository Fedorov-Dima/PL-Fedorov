a = []
n = int(input('Длина масива '))
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
a.sort()
for i in a:
    if i % 2 != 0:
        print(i)
        break
