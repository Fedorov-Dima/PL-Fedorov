a = []
print('Вводите целые числа:')
for i in range(10):
    a.append(int(input()))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)
