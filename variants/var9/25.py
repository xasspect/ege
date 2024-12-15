from fnmatch import *

for x in range(159, 10 ** 7, 159):
    if fnmatch(str(x), '2?1*67'):
        print(x, x // 159)