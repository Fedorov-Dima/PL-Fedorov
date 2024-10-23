a = input()
a = a[:int(len(a)/2)].replace('п', '*') + a[int(len(a)/2):]
print(a)
