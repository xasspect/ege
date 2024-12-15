from fnmatch import *
for x in range(169, 10 ** 9, 169):
    if fnmatch(str(x), '123*567?'):
        print(x, x//169)