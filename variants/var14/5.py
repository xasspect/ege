def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(2, 10000):
    s = f(n)
    x1 = s.count('0')
    x2 = s.count('1')
    if x1 == x2:
        s += s[-1]
    if x1 > x2:
        s += '1'
    if x1 < x2:
        s += '0'

    if x1 == x2:
        s += s[-1]
    if x1 > x2:
        s += '1'
    if x1 < x2:
        s += '0'

    if x1 == x2:
        s += s[-1]
    if x1 > x2:
        s += '1'
    if x1 < x2:
        s += '0'

    r = int(s, 2)
    if n > 80 and r % 2 == 0:
        if 2 * r + 2:
            print(n, r)
