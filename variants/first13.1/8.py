from itertools import permutations
k = 0
a = permutations('01234567', r=6)

k = []
for x in a:
    s = ''.join(x)
    if s[0]!='0':
        if s.count('3') == 0:
            for i in range(len(s) - 1):
                if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0:
                    k.append(s)
print(len(set(k)))
