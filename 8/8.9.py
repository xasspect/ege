from itertools import *
a = product('0123456789AB', repeat=5)

k = 0
for x in a:
    z = ''.join(x)
    if z[0] != '0' and z.count('7') == 1 and z.count('9') + z.count('A') + z.count('B') <= 3:
        k += 1


print(k)