a = []
# n = int(input('Длина масива '))
print('Вводите числа')
for i in range(10):
    a.append(int(input()))
b = []
print('Вводите числа')
for i in range(10):
    b.append(int(input()))
a, b = b, a
print(a)
print(b)
