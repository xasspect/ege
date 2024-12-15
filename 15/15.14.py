for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not(((x % 15 == 0) and (x % 10 != 0)) <= (a < x + 50)):
            fl = False
            break

    else:
        print(a)