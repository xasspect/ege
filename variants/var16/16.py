def f(n):
    if n >= 2030: return n
    if n < 2030: return n + 2 + f(n + 2)

def g(m):
    if m <= 2030: return m
    if m >2030: return m - 2 + g(m - 2)

print(g(2100) - f(2100))