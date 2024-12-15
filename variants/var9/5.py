def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 100):
    s = f(n)
    if n % 2 == 0:
        s += '01'
    else:
        s += '10'

    r = int(s, 2)
    if r > 73:
        print(n)
