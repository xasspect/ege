from itertools import *
a = product('0123456789abcde', repeat=5)
k = 0
for x in a:
    x = ''.join(x)
    if x[0]!='0' and x.count('8') == 1 and x.count('a') + x.count('b') +  x.count('c') + x.count('d') + x.count('e') >= 2:
        k += 1

print(k)