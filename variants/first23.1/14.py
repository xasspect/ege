a = '0123456789ABCDEFGHIJKLMN'
for x in a:
    x1 = int(f'4M{x}F', 24)
    x2 = int(f'265AFDN{x}', 24)
    x3 = int(f'N4{x}931B3L', 24)
    x4 = int(f'NG{x}4F', 24)
    x5 = int(f'FKJB5{x}IK', 24)
    if (x1 + x2 + x3 + x4 + x5) % 23 == 0:
        print(x, (x1 + x2 + x3 + x4 + x5)// 23)
