lst = [int(i) for i in input().split(' ')]

# Стандартный проход
all_positive = True
any_null = False
all_even = True
any_odd = False

for i in lst:

    if i < 0:
        all_positive = False

    if i == 0:
        any_null = True

    if i % 2 != 0:
        all_even = False
        any_odd = True

print(f""""
           all_positive = {all_positive}
           any_null = {any_null}
           all_even = {all_even}
           any_odd = {any_odd}""")

# С помощью функций
all_positive = all(i > 0 for i in lst)
any_null = any(i == 0 for i in lst)
all_even = all(i % 2 == 0 for i in lst)
any_odd = not all_even

print(f""""
           all_positive = {all_positive}
           any_null = {any_null}
           all_even = {all_even}
           any_odd = {any_odd}""")