for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not((x % a == 0) or ((70 <= x <= 90) <= (x % 22 != 0))):
            fl = False
            break
    else:
        print(a)