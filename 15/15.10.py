s = []

for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x <= 19) or (y < 2 * x + a - 50) or (y > 17)):
                fl = False
                break
        if fl == False:
            break
    else:
        print(a)
