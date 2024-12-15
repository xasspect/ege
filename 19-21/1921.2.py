def f(s, n):
    if s < 20: return n % 2 == 0
    if n == 0: return 0
    h = [f(s - 2, n - 1), f(s - 5, n - 1), f(s / 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print('19', [s for s in range(20, 100) if f(s, 2)])
print('19', [s for s in range(20, 100) if not f(s, 1) and f(s, 3)])
print('19', [s for s in range(20, 100) if not f(s, 2) and f(s, 4)])
