a = []
n = int(input('Длина масива '))
print('Вводите числа')
for i in range(n):
    a.append(int(input()))
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
if len(b) > 0:
    b.sort()
    b.reverse()
    print(b)
else:
    print('нечётных чисел нет')
