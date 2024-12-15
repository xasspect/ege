def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

k = []
for n in range(1, 100):
    s = f(n)
    if s.count('1') % 2 == 0:
        s += '00'
        s = '11' + s[2:]
    else:
        s += '11'
        s = '10' + s[2:]
    if s.count('1') % 2 == 0:
        s += '00'
        s = '11' + s[2:]
    else:
        s += '11'
        s = '10' + s[2:]

    r = int(s, 2)
    k.append(r)
print(max(k))
