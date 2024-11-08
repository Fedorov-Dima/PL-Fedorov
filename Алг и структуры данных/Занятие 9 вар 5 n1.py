z = []
n = int(input('Введите n: '))
m = int(input('Введите m: '))
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    a.sort()
    z.append(a)
for i in range(n):
    print(z[i])