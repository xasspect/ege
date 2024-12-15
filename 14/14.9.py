def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3
    return str(b)

t = 3 ** 2000 + 3 ** 10
for i in range(59000, 60000):
    s = t - i
    if f(s).count('2') == 2000:
        print(i)



