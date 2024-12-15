def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 100):
    s = f(n)
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    print(r)