from itertools import *

a = permutations(sorted('амфибрахuй'), r=10)
k = 0
for x in a:
    x = ''.join(x)

    if x[:2] == 'ам' and (x[-2:] == 'ий' or x[-2:] == 'uй'):
        k += 1
print(k)
