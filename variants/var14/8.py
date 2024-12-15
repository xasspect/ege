from itertools import *
a = product(sorted('СОЛНЦЕ'), repeat=6)
k = 0
for x in a:
    x = ''.join(x)
    if x.count('Ц') == 1:
        if x.count('О') <= 2:
            k += 1
print(k)