from fnmatch import *
for x in range(98591, 10 ** 10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)