def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

k = []

for n in range(1, 1000):
    s = f(n)
    if n % 2 == 0:
        s += '00'
    else:
        s += '11'
    r = int(s, 2)
    if r > 115:
        print(r)
