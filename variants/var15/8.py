from itertools import *
a = product('01234567', repeat=5)
k = 0
for x in a:
    x = ''.join(x)
    if x[0]!='0':
        if int(x[0]) % 2 == 0 and x[-1] != '2' and x[-1] !='6' and x.count('7') <= 2:
            k += 1
print(k)
