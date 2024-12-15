c = [s for s in range(30, 46)]

for a in range(1, 100):
    fl = True
    for x in range(1, 100):
        if not(((x % a == 0) and (x in c)) <= (x % 12 != 0)):
            fl = False
            break
    else:
        print(a)