def nod(x, y):
    while x * y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y

def nod3(x, y):
    if x * y == 0:
        return x + y
    if x < y:
        return nod3(x, y % x)
    else:
        return nod3(x % y, y)

def f(a, b, c, d):
    y = b * d
    x = abs(a * d - c * b)
    z = nod3(x, y)
    x //= z
    if c / d > a / b:
        x = -x
    y //= z
    if x * y == 0:
        print(0)
        return
    print(x)
    print('-')
    print(y)

a = int(input())
print('-')
b = int(input())
print('')
c = int(input())
print('-')
d = int(input())
print('')
f(a, b, c, d)