from random import randint

p = float(input())
mass = [randint(1, 5) for i in range(5)]

print(p >= sum(mass))