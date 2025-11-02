a = int(input())
b = int(input())

# Решение здорового человека:
# print("max:", max(a, b))
# print("min:", min(a, b))

# Решение курильщика:
if a >= b:
    print("max:", a)
else:
    print("max:", b)

if a <= b:
    print("min:", a)
else:
    print("min:", b)