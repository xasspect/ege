def f(n):
    b = ''
    while n:
        b = str(n % 6) + b
        n //= 6
    return b

a = []
for n in range(1, 100):
    s = f(n)

    if n % 3 == 0:
        s = s + s[:2]
    else:
        s = s + f(n % 3 * 10)
    r = int(s, 6)
    print(n, r)
    if r > 680:
        a.append(r)
print(min(a))
