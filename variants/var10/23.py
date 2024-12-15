def f(s, end):
    if s > end or s == 26: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s * 2, end)

print(f(2, 11) * f(11, 39))