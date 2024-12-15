b = [x for x in range(70, 91)]
for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        if not((x % a == 0) or ((x in b) <= (x % 22 != 0))):
            fl = False
            break
    else:
        print(a)