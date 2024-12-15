from itertools import *

a = list(permutations(sorted('ХОЧУНАБЮДЖЕТ'), r=12))
f = list(permutations(sorted('ОУАЮЕ'), r=5))

s = []

for u in f:
    u = ''.join(u)
    s.append(u)

k = c = 0
# for x in a:
#     k += 1
#     x = ''.join(x)


print(s)