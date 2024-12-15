from itertools import *
a = list(product(sorted('ЛЮСТРА'), repeat=5))
k = 0
for x in a:
    x = ''.join(x)
    if x.count('Ю') <= 2 and x[-1] != 'Л' and x[-1] != 'С' and x[-1] != 'Т' and x[-1] != 'Р':
        k += 1
print(k)