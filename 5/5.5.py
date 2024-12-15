for i in range(1, 100):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '11'
    if int(s, 2) > 114:
        print(int(s, 10))
        break