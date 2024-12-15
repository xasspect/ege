def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3
    return b

def b(e):
    x1 = []
    x2 = []
    for i in e:
        if int(i) % 2 == 0:
            x1.append(i)
        else:
            x2.append(i)
    if len(x1) > len(x2):
        return 1
    else:
        return 0


k = []
for n in range(11, 1000):
    s = f(n)
    if b(s) == 1:
        s = '22' + s
    else:
        s = '11' + s
    r = int(s, 3)
    if r > 100:
        k.append(r)
print(min(k))
