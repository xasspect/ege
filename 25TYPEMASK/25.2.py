from fnmatch import *
for x in range(2025, 10**10, 2025):
    if fnmatch(str(x), '21?3*145?5'):
        print(x, x//2025)