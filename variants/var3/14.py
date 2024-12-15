def f(n, c):
    b = ''
    while n:
        b = str(n % c) + b
        n //= c
    return b

for x in range(2, 10):
    s = 7 ** 500 - int(f(53, x))
    if s % 6 == 0:
        print(x)