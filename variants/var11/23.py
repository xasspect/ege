def f(s, end):
    if s > end or s == 11 or s == 18: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s + 2, end) + f(s * 3, end)

print(f(4, 8) * f(8, 23))
