def f(s, end):
    if s > end or s == 15: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s * 2, end)

print(f(2, 12) * f(12, 32))