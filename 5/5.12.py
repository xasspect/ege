def f(n):
    b = ''
    while n > 0:
        b += str(n % 2)
        n //= 2
    return b[::-1]

for n in range(1, 100000):
    s = f(n)
    s = s + s[-1]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    r = int(s, 2)
    if r < 13500:
        print(r)




