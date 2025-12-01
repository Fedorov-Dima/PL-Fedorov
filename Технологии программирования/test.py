# Теория информации
from math import log

groups = {}

def f(a, id=''):
    a.sort(reverse=True)
    a1 = [a[0]]
    a0 = a[1:]
    while round(abs(sum(a1) - sum(a0)), 2) > sum(a) / 2:
        if sum(a1) < sum(a0):
            a1.append(a0.pop(0))
        elif sum(a1) > sum(a0):
            a0.append(a1.pop(0))
        if len(a1) == len(a0) == 1 and sum(a1) != sum(a0):
            break
    print(a1, a0, round(abs(sum(a1) - sum(a0)), 2))
    if len(a1) == 1:
        groups[id + '1'] = a1[0]
    else:
        f(a1, id + '1')
    if len(a0) == 1:
        groups[id + '0'] = a0[0]
    else:
        f(a0, id + '0')

a = [0.5, 0.2, 0.1, 0.1, 0.05, 0.05]
# a = [0.46, 0.35, 0.12, 0.03, 0.03, 0.01]
f(a, '')
print(groups)
n = 2
groups_copy = list(groups)
L = sum([a[i] * len(groups_copy[i]) for i in range(len(a))])
H_a = sum([i * log(i, 2) for i in a]) * -1
R_a = L - H_a
C = n * L
print(L)
print(H_a)
print(R_a)
print(C)
