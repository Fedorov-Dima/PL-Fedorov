n = int(input())
r = 1
for i in range(2, n + 1):
  r += r * i
print(r)
