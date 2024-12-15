def f(n, s):
    b = ''
    x1 = bin(n)[2:]
    x2 = bin(s)[2:]

    while len(x2) != len(x1):
        x2 = '0' + x2

    for i in range(len(x1)):
        if x1[i] == x2[i]:
            b = b + str(x1[i])
        else:
            b = b + '0'
    return int(b, 2)

for a in range(1, 1000):
    fl = True
    for x in range(90, 101):
        if not((f(x, 79) != 0) and ((f(x, 31) == 0) <= (f(x, a) == 0))):
            fl = False
            break
    else:
        print(a)
