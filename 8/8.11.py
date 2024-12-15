from itertools import *

a = product(sorted('ФОКУС'), repeat=5)

k = 0
for x in a:
    k += 1
    x = ''.join(x)
    if x.count('Ф') == 0 and x.count('У') == 2:
        print(k)
