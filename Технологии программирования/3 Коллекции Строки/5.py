st = input('строка: ').lower()
a = input('дайте букаву: ')
if a in st:
    print(st.index(a))
    print(st.rfind(a))
else:
    print('соответствующее сообщение')