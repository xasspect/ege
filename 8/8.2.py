from itertools import product


a = list(product('АГИЛМОРФ', repeat=5))

k = 0
count = 0
for n in a:
    k += 1
    x = ''.join(n)

    if x[2:] != 'ЛМ' and x.count('И') >= 2 and k % 2 == 0:
        print(k, x)
        count += 1
print(count)


