def f(a, b, m):
    if a * b >= 455: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19', [s for s in range(1, 91) if f(5, s, 2)]) # 23
print('20', [s for s in range(1, 91) if not f(5, s, 1) and f(5, s, 3)])
print('21', [s for s in range(1, 91) if not f(5, s, 2) and f(5, s, 4)])
