for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((108 % x == 0) <= (x % y != 0)) or (x + y > 80) or (a - y > x)):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)