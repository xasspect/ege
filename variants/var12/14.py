def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3
    return b

for x in range(21, 30):
    s = f(x)
    if str(s)[-2:] == '11':
        print(x)