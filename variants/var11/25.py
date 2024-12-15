from fnmatch import *
for x in range(1923, 10 ** 8, 1923):
    if fnmatch(str(x), '1*2??76'):
        print(x, x//1923)
