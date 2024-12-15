s = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156

def f(n):
    b = ''
    while n:
        b = str(n % 25) + b
        n //= 25
    return b
print(f(s))
