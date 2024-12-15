def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 1000):
    s = f(n)
    if s.count('1') % 4 == 0:
        s = '10' + s
    else:
        s = '11' + s
    if s.count('1') % 2 == 0:
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r <= 250:
        print(n)
