from sys import *

setrecursionlimit(3000)

def f(n):
    if n == 1: return n
    if n > 1: return 2 * n * f(n - 1)

print((f(2024) // 16 - f(2023)) / f(2022))