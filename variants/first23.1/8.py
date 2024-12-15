from itertools import product

a = list(product(sorted('УДАЧ'), repeat=5))
k = []
for n in a:

    x = ''.join(n)
    if x[0] == 'У' or x[0] == 'А':
        k.append(x)
p = 0
for i in k:
    p += 1
    if i == 'УДАЧА':
        print(p)