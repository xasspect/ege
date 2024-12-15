k = 0

b = [str(x) for x in range(120, 131)]

for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        if not(((str(x) in b) <= (x % 7 != 0)) or (a > (2 * x))):
            fl = False
            break
    else:
        print(a)
