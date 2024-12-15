from itertools import *

a = product(sorted('ПЛЮСЕНОК'), repeat=7)
k = 0
for x in a:
    x = ''.join(x)
    if x[0] != 'П' and x[0] != 'Л' and x[0] != 'С' and x[0] != 'Н' and x[0] != 'К':

        for i in range(len(x) - 1):


            if x[-1] == 'Е':
                if x[-2] == 'Ю' or x[-2] == 'Е' or x[-2] == 'О':
                    k += 1
            elif x[i] == 'Е':
                if (x[i - 1] != 'П' and x[i + 1] != 'П') and (x[i - 1] != 'Л' and x[i + 1] != 'Л') and (x[i - 1] != 'С' and x[i + 1] != 'С') and (x[i - 1] != 'Н' and x[i + 1] != 'Н') and (x[i - 1] != 'К' and x[i + 1] != 'К'):
                    k += 1
print(k)
