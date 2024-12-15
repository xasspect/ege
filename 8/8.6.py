from itertools import permutations

a = permutations('матвей', r=6)

k = 0
for x in a:
    x = ''.join(x)
    if x[0] != 'й' and 'ае' not in x:
        k += 1
print(k)