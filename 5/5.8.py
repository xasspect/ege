for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '11'
    else:
        s += '01'

    r = int(s, 2)
    if r > 61:
        print(r)