def f(s, end):
    if s < end or s == 20:return 0
    if s == end: return 1
    return f(s - 2, end) + f(s - 3, end) + f(s // 5, end)

print(f(41, 10) * f(10, 5))