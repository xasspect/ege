def f(n):
    b = ''
    while n:
        b = str(n % 6) + b
        n //= 6
    return b

for x in range(2031):
    n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    s = f(n)
    if s.count('0') == 202:
        print(x)
