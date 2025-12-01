from math import log
groups = {}

def s(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                z = a[i]
                a[i] = a[j]
                a[j] = z
    return a

def f(a, id=''):
    a.sort(reverse=True)
    # a = s(a)
    a1 = [a[0]]
    a0 = a[1:]
    min_sum = 999
    while round(abs(sum(a1) - sum(a0)), 2) != min_sum:
        if len(a1) == len(a0) == 1:
            break
        if round(abs(sum(a1) - sum(a0)), 2) < min_sum:
            min_sum = round(abs(sum(a1) - sum(a0)), 2)
        if sum(a1) < sum(a0):
            a1.append(a0.pop(0))
        elif sum(a1) > sum(a0):
            a0.append(a1.pop(0))
        # print(min_sum)
        # print(a1, a0)
        # print(round(abs(sum(a1) - sum(a0)), 2))

    print(a1, a0, min_sum)

    if len(a1) == 1:
        groups[id + '1'] = a1[0]
    else:
        f(a1, id + '1')
    if len(a0) == 1:
        groups[id + '0'] = a0[0]
    else:
        f(a0, id + '0')

a = [0.49, 0.28, 0.08, 0.07, 0.06, 0.02]
# a = [0.46, 0.35, 0.12, 0.03, 0.03, 0.01]
f(a, '')
print(groups)
n = 4
groups_copy = list(groups)
L = sum([a[i] * len(groups_copy[i]) for i in range(len(a))])
H_a = sum([i * log(i, 2) for i in a]) * -1
R_a = L - H_a
C = n * L
print(L)
print(H_a)
print(R_a)
print(C)