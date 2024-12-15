from itertools import product

a = list(product((sorted('ШКОЛА')), repeat=5))

k = 0

for x in a:
    k += 1
    x = ''.join(x)
    if x == 'ШАЛАШ':
        print(k, x)