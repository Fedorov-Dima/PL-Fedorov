a = []
print('Вводите целые числа:')
for i in range(10):
    a.append(int(input()))
for i in range(1, 10):
    if a[i - 1] < 0 and a[i] < 0:
        print(a[i - 1], a[i])
