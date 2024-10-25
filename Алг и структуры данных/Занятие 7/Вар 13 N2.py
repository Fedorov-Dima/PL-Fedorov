a = []
# n = int(input('Длина масива '))
print('Вводите числа')
for i in range(8):
    a.append(int(input()))
for i in range(len(a)):
    if a[i] < 15:
        a[i] *= 2
print(a)
