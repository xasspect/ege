for x in range(22):
    for y in range(22):
        x1 = sum([c * 21 ** i for i, c in enumerate([9, 4, 3, 6, 9, 7, x, 2, 1][::-1])])
        x2 = sum([c * 21 ** i for i, c in enumerate([2, y, 9, 2, 5, 3][::-1])])
        if (x1 - x2) % 20 == 0:
            print( 1// 20)