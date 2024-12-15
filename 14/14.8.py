a = '0123456789ABCD'
for x in a:
    x1 = int(f'1{x}563', 14)
    x2 = int(f'871{x}3', 14)
    if (x1 + x2) % 24 == 0:
        print(x, (x1 + x2)//24)