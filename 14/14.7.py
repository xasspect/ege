a = '0123456789ABCDE'
for x in a:
    x1 = int(f'123{x}5', 15)
    x2 = int(f'1{x}233', 15)
    if (x1 + x2) % 14 == 0:
        print(x, (x1 + x2)//14)