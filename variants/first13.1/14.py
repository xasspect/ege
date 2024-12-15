def f(n):
    b = ''
    while n:
        b = str(n % 9) + b
        n //= 9
    return b

s = 81 ** 820 - 9 ** 761 - 3 ** 2022 + 14
print(f(s).count('8'))
