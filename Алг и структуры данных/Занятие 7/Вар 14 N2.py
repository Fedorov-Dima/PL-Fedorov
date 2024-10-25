a = []
# n = int(input('Длина масива '))
print('Вводите числа')
for i in range(10):
    a.append(int(input()))
s = sum(a) / len(a)
for i in range(len(a)):
    if a[i] > s:
        a[i] = 1
print(a)
