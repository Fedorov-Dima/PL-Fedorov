z = []
n = int(input('Введите n: '))
m = int(input('Введите m: '))

for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    if a[a.index(min(a))] % 2 == 0:
        a[a.index(min(a))] = 0
    else:
        a[a.index(min(a))] = 1
    z.append(a)

for i in range(n):
    print(z[i])