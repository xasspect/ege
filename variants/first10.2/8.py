from itertools import *
a = product('0123456789', repeat=3)
k = 0
for x in a:
    x = ''.join(x)
    s = [int(x) for x in x]
    if s[0] != 0 and  s[0] <= s[1] and s[1] <= s[2]:
        k += 1
print(k)



