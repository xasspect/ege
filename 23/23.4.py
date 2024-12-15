def f(s, end):
    if s < end: return 0
    if s == end: return 1
    return f(s - 2, end) + f(s // 2, end)

print(f(32, 14) * f(14, 1))