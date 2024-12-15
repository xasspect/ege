a = []
for a1 in range(1, 101):
    for a2 in range(1, 101):
        fl = True
        for x in range(1, 101):
            if (15 <= x <= 40) <= (((21 <= x <= 63) and (a1 >= x >= a2)) <= (15 >= x >= 40)) == False:
                fl = False
                break
        if fl:
            a.append(a2 - a1)
print(a)


