#def f(z, m):
#    if z < 10:
#        m = max(m, z)
#        return m
#    else:
#        m = max(m, z - z // 10 * 10)
#        z //= 10
#        return f(z, m)
#
#z = int(input())
#print(f(z, 0))

def f(m=0):
    z = int(input())
    if z == 0:
        return m
    else:
        m = max(m, z)
        return f(m)
print(f(0))