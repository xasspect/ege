from itertools import *
k= 0
a = product(sorted('МЫСЛЬ'), repeat=5)
for x in a:
    k += 1
    x = ''.join(x)
    if x[0] == 'Ы' and x[1] == 'Ы':
        print(k)