for x in range(2031):
    s = 7 ** 170 + 7 ** 100 - x
    a = []
    while s > 0:
        a = [s%7] + a
        s //= 7
    if a.count(0) == 71:
        print(x)
    print(a)