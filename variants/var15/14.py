a = '0123456789abcdefghijkl'

for x in a:
    x1 = int(f'18{x}89957', 22)
    x2 = int(f'80{x}33', 22)
    x3 = int(f'521{x}6', 22)
    if (x1 + x2 + x3) % 21 == 0:
        print(x, (x1 + x2 + x3) // 21)