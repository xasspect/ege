def f(s, end):
    if s > end: return 0
    if s == end: return 1
    return f(s + 2, end) + f(s * 2, end)

print(f(1, 24) * f(24, 50))