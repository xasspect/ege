from itertools import *
a = permutations(sorted('КРОВЬ'), r=5)
k = 0
for x in a:
    x = ''.join(x)
    if x[0] != 'Ь':
        if 'ЬО' not in x and 'ОЬ' not in x:
            k += 1
print(k)
