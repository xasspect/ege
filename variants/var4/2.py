print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or (y and (not(z)))) and (not(w))
                print(x, y, z, w, int(f))