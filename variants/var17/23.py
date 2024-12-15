def f(s, end):
    if s < end: return 0
    if s == end: return 1
    return f(s - 2, end) + f(s - 5, end)

print(f(24, 3))