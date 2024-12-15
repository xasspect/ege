def f(s, end):
    if s > end: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s + 3, end) + f(s * 3, end)

print(f(3, 9) * f(9, 27) * f(27, 31))