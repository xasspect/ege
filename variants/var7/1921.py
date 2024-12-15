def f(a, b, m):
    if a + b >= 79: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a + b, b, m - 1), f(a, b + a, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19', [s for s in range(1, 70) if f(9, s, 2)]) # 21
print('20', [s for s in range(1, 70) if not f(9, s, 1) and f(9, s, 3)])
print('21', [s for s in range(1, 70) if not f(9, s, 2) and f(9, s, 4)])
