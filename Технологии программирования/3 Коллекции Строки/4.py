st = input('строка: ').lower()
subst = input('подстрока: ').lower()
if subst in st:
    print('Подстрока есть')
else:
    print('Подстроки нет')