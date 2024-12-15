from itertools import *

a = product(sorted('АРГУМЕНТ'), repeat=4)
print(sorted('АРГУМЕНТ'))
k = 0
for x in a:
    k += 1
    x = ''.join(x)
    if x == 'АГЕМ' or x == 'ГЕМН' or x == 'ЕМНР' or x == 'МНРТ' or x == 'НРТУ':
        print(k, x)
