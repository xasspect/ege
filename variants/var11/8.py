from itertools import *

a4 = product(sorted('ЧОАНИМЕ'), repeat=4)
a5 = product(sorted('ЧОАНИМЕ'), repeat=5)
a6 = product(sorted('ЧОАНИМЕ'), repeat=6)

k = 0

for x in a4:
    x = ''.join(x)
    if x.count('М') == 3:
        k += 1

for x in a5:
    x = ''.join(x)
    if x.count('М') == 3:
        k += 1

for x in a5:
    x = ''.join(x)
    if x.count('М') == 3:
        k += 1
print(k)
