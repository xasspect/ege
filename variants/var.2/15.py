b = [x for x in range(80, 101)]

for a in range(1, 150):
    fl = True
    for x in range(1, 150):
        if not((x % 17 == 0) <= ((not(x in b)) or (a < x + 30))):
            fl = False
            break
    else:
        print(a)