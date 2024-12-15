def f(n):
    b = ''
    while n:
        b = str(n % 8) + b
        n //= 8
    return b
k = 0
for n in range(1, 1000):
    s = f(5)
    if n % 7 == 0:
        s = s + s[-2:]
    else:
        e = (n % 7) * 7
        y = f(e)
        s = s + str(y)
    r = int(s, 8)
    if r < 3000:
        k += 1
print(k)