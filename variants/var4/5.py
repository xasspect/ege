def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 100):
    s = f(n)
    if n % 2 != 0:
        s = '10' + s + '11'
    else:
        s = '1' + s + '00'
    r = int(s, 2)
    if r > 1023:
        print(r)
