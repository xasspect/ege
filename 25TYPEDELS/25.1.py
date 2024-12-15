def f(n):
    s = set()
    for i in range(10, int(n**0.5) + 1):
        if n % i == 0: s |= {i, n//i}
    return sorted(s)

for n in range(800001, 801000):
    s = [i for i in f(n) if i % 10 == 9]
    if len(s) > 0:
        print(n, min(s))
