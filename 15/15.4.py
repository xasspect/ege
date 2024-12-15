for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not((x % a != 0) <= ((x % 28 == 0) <= (x % 49 !=0))):
            fl = False
            break
    else:
        print(a)
