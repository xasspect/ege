def f(s, end):
    if s > end: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s * 2, end)

print(f(4, 8) * f(8, 10) * f(10, 15))