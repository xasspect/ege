for i in range(1, 100):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    if int(s, 2) > 64:
        print(int(s, 2))
        break
