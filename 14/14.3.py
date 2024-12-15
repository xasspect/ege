for x in range(2031):
    s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    a = []
    while s > 0:
        a = [s%6] + a
        s //= 6
    if a.count(0) == 202:
        print(x)
