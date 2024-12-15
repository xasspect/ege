def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3
    return b

print(f(2 * 27 ** 7 + 3 ** 10 - 9).count('0'))