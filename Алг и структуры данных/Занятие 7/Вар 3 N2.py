a = []
print('Вводите числа')
for i in range(8):
    a.append(int(input()))
for i in range(8):
    if a[i] < 15:
        a[i] *= 2
print(a)
