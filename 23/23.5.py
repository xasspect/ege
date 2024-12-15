def f(s, end):
    if s > end: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s + 2, end) + f(s + 3, end)

print(f(5, 7) * f(7, 11))