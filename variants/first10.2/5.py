def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

k = []
for n in range(1, 1000):
    s = f(n)
    b = f(n)
    if sum(map(int, s)) % 2 == 0:
        s += '0'
        s = '1' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]
    r = int(s, 2)

    if r > 49:
        if r == 50:
            print(n)
