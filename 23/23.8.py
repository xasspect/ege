def f(s, end):
    if s > end: return 0
    if s == end: return 1
    return f(s + 1, end) + f(s + 2, end) + f(s * 2, end)

print(f(4, 11) * f(11, 13) * f(13, 15))
