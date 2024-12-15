from itertools import *
k = 0
a = product('012345678', repeat=5)
for x in a:
    x = ''.join(x)
    if x[0] != '0':
        if int(x[0]) % 2 == 0:
            if x[-1] != '1' and x[-1] !='8':
                if x.count('3') == 1 or x.count('3') == 0:
                    k += 1
print(k)