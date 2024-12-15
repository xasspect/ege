def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

k = []
for n in range(1, 256):
    s = f(n)
    if n % 2 == 0:
        s = '11' + s + '0'
    else:
        s = '1' + s + '00'
    r = int(s, 2)
    k.append(r)
t = [int(x) for x in k if k.count(x) == 2]
print(len(t))

