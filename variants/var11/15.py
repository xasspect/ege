for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not( ((x % 34 == 0) and (x % 51 != 0)) <= ((x % a != 0 ) or (x % 51 == 0)) ):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)