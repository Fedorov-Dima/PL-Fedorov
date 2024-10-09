n = int(input())
r = 1
x = 1
for i in range(2, n + 1):
  x *= i
  r += x
print(r)
