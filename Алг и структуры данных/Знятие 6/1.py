s = input()
s = s.split(' ')
c = 0
for i in s:
    if i[0] == 'е':
        c += 1
print(c)
