for i in range(1, 100):

    i = bin(i)[2:]
    if i.count('1') % 2 == 1:
        i = i + '1'

    if i.count('1') % 2 == 1:
        i = i + '1'

    if int(i, 2) > 43:
        print(int(i, 2))
        break


