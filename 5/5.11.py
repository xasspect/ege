def f(n):
    b = ''
    while n > 0:
        b += str(n % 3)
        n //= 3
    return b[::-1]

for n in range(1, 10000):
    s = f(n)
    if int(s) / 7:
        s = s + s[-2:]


    r = int(s, 3)
    if r > 369:
        print(r)
        break

