from itertools import*

a = product('012345678', repeat=7)
k = 0
for x in a:
    x = ''.join(x)
    if x[0]!='0':

        if x.count('8') == 1:
            if int(x[0]) % 2 == 0 and int(x[-1]) % 2 != 0:
                k += 1
print(k)