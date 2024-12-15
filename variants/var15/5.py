def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 100):
    s = f(n)
    if s.count('1') % 2 == 0:
        s = '11' + s[2:] + '00'
    else:
        s = '10' + s[2:] + '11'
    if s.count('1') % 2 == 0:
        s = '11' + s[2:] + '00'
    else:
        s = '10' + s[2:] + '11'
    r = int(s, 2)
    print(r)