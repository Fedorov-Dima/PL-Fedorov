a = int(input())
b = int(input())
print(' '.join([str(i) for i in range(min(a, b), max(a, b) + 1)]))
print('\n'.join([str(i) for i in range(max(a, b), min(a, b) + 1, -1)]))