from sys import *
setrecursionlimit(3000)


def f(n):
    if n < 3: return 3
    if n >= 3: return 2 * n + 5 + f(n - 2)

print(f(3027) - f(3023))
