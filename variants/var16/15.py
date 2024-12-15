for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not( ((x % 4 !=3) or (x % 6 != 1)) <= (x % 36 != a)  ):
            fl = False
            break
    else:
        print(a)