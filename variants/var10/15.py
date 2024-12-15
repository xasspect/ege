for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not( (x < a) or (y < a) or (x + 2 * y > 150) ):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)