def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3

    return b
k = []
for n in range(1, 1000):
    s = f(n)
    t = n % 3
    if t == 0:
        s += s[:2]
    else:
        t *= 5
        s += f(t)
    r = int(s, 3)
    if r > 64:
        k.append(r)
print(min(k))

