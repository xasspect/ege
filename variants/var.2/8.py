from itertools import *
k = 0

a = product(sorted('ГИРЛЯНДА'), repeat=6)

for x in a:
    k += 1
    x = ''.join(x)
    if k % 2 == 0:
        if x[0] != 'Я':
            if x.count('Д') == 3:
                print(k, x)
