def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

k = 0
for n in range(1, 10000):
    t = n * 2
    s = f(t)
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    r = int(s, 2)
    if r > 1017:
        print(n)

