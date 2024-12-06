def f(n):
    if n >= 10:
        print(n - n // 10 * 10)
        f(n // 10)
    else:
        print(n)

f(int(input()))