
for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not( (((x ** 2) > 16) or (a > x)) and ((y ** 2 <= 81) or (a <= y)) ):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)