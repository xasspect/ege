def f(s, end):
    if s < end or s == 24: return 0
    if s == end: return 1
    return f(s - 2, end) + f(s - 3, end) + f(s // 4, end)

print(f(36, 13))