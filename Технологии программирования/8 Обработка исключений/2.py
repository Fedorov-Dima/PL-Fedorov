def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as err:
    print(f"Ошибка {err}! x и y должны быть целыми числами!")
except RecursionError as err:
    print(f"Ошибка {err}! Слишком большой y!")