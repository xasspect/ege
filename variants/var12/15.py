for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not( ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0)) ):
            fl = False
            break
    else:
        print(a)