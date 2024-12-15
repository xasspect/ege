from itertools import *
s = 0
a = permutations(sorted('КАРПЫ'), r=5)
for x in a:
    x = ''.join(x)
    if x[0] != 'Р' and x[-1] != 'Р':

        for i in range(len(x) - 1):
            if x[i] == x[0] and x[i] == 'А':
                if x[i + 1] != 'Ы':
                    s += 1
            elif x[i] == x[0] and x[i] == 'Ы':
                if x[i + 1] != 'А':
                    s += 1
            elif x[i + 1] == x[4] and x[i + 1] == 'А':
                if x[i] != 'Ы':
                    s += 1
            elif x[i + 1] == x[4] and x[i + 1] == 'Ы':
                if x[i] != 'А':
                    s += 1
            else:
                if x[i] == 'Ы' and x[i - 1] != 'А' and x[i + 1] != 'А':
                    s += 1
                elif x[i] == 'А' and x[i - 1] != 'Ы' and x[i + 1] != 'Ы':
                    s += 1
print(s)


