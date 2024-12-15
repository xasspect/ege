k = 0
def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

for n in range(1, 100):
    s = f(n)
    if s.count('1') % 2== 0:
        s += '00'
    else:
        s += '10'
    r = int(s, 2)
    if 64 <= r <= 72:
        print(n)