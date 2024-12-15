def f(n):
    b = ''
    while n:
        b = str(n % 6) + b
        n //= 6
    return b

s = 5 * 36 ** 7 + 6 ** 10 - 36
print(f(s).count('5'))
