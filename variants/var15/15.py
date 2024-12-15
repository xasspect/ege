for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not( ((x % 6 == 0) <= (x % 14 != 0)) or (x + a >= 70) and (a % 20 == 0) ):
            fl = False
            break
    else:
        print(a)
