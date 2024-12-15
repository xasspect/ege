def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: s |= {i, n // i}
    return sorted(s)

for x in range(700001, 701000):
    t = f(x)
    if len(t) > 0 and (max(t) + min(t)) % 10 == 4:
        print(x, (max(t) + min(t)))