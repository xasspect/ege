for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not( (x > 56) or (y >= x) or (3 * x - y < a) ):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)
