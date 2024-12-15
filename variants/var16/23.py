def b(n):
    t = []
    for x in str(n):
        t.append(int(x))
    return t


def f(s, end):
    if s < end: return 0
    if s == end: return 1
    return f(s - sum(b(s)), end) + f(s // 2, end) + f(s - 1, end)

print(f(40, 25) * f(25, 10))