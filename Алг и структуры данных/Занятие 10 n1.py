f1 = open('ФедоровДмитрийИгоревич_У-242_vvod.txt', 'r')
z = f1.readlines()
for i in range(len(z)):
    z[i] = z[i].split(' ')
    z[i] = [int(z[i][j]) for j in range(len(z[i]))]
    z[i].sort()
    z[i] = [str(z[i][j]) for j in range(len(z[i]))]
f1.close()
f2 = open('ФедоровДмитрийИгоревич_У-242_vivod.txt', 'w')
for i in z:
    f2.write(f'{' '.join(i)}\n')
f2.close()