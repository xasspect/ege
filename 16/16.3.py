from sys import *

setrecursionlimit(3000)


def f(n):
    if n == 1: return 1
    if n > 1: return (n - 1) * f(n - 1)

print((f(2024) // 7 - f(2023)) / f (2022))