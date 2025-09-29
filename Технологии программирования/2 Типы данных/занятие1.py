R1 = float(input())
R2 = float(input())
print(round(R1 + R2, 2))
print()

m = int(input())
print(m // 60, "часов")
print((m / 60 - m // 60) * 60, "минут")
print()

m = -5
n = 4
a, b, c = 1, 1, 0
# a * x ** 2 + b * x + c == 0
x = int(input())
print(m <= a * x ** 2 + b * x + c <= n)