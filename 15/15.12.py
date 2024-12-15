for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x + y <= 30) or (y <= x + 2) or (y >= a)):
                fl = False
                break

        if fl == False:
            break
    else:
        print(a)
