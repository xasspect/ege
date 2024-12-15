for x in range(0, 100000):
    s = 3 ** 2000 + 3 ** 10 - x
    while s > 0:
        if s % 3 == 0:
            if str(s).count('2') == 2000:
                print(x)
        s //= 3