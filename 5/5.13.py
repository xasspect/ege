def f(n):
    b = ''
    while n > 0:
        b += str(n % 2)
        n //= 2
    return b[::-1]

for n in range(1, 1000):
    s = f(n)
    if s.count('1') % 2 == 0:
        s += '1'
    else:
        s += '0'
    if int(s, 2) % 2 == 0:
        s += '10'
    else:
        s += '01'

    r = int(s, 2)
    if r < 1000:
        print(r)