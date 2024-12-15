from itertools import product, permutations

a = list(product('АПРСУ', repeat=5))
k = 0
for n in a:
    k+=1
    x = ''.join(n)
    if x.count('У') <= 1 and 'АА' not in x:
        print(k, x)