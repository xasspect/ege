def f(s, end):
    if s < end or s == 5: return 0
    if s == end: return 1
    return f(s - 1, end) + f(s // 2, end) + f(s // 3, end)

print(f(26, 11) * f(11, 2))