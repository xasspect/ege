def f(s, end):
    if s < end or s == 32: return 0
    if s == end: return 1
    return f(s - 1, end) + f(s - 5, end)

print(f(42, 23) * f(23, 22) * f(22, 9))