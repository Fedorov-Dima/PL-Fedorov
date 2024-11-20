f1 = open('ФедоровДмитрийИгоревич_У-242_vvod.txt', 'r')
f2 = open('ФедоровДмитрийИгоревич_У-242_vivod.txt', 'w')
z = f1.readlines()
for i in range(len(z)):
    z[i] = z[i].split(' ')
    z[i] = [int(z[i][j]) for j in range(len(z[i]))]
    if z[i][z[i].index(min(z[i]))] % 2 == 0:
        z[i][z[i].index(min(z[i]))] = 0
    else:
        z[i][z[i].index(min(z[i]))] = 1
    z[i] = [str(z[i][j]) for j in range(len(z[i]))]
    f2.write(f'{' '.join(z[i])}\n')
f1.close()
f2.close()
