from fnmatch import *
for x in range(183, 10 ** 9, 183):
    if fnmatch(str(x), '??287*139'):
        print(x, x//183)