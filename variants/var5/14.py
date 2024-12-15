a = '0123456789ABCDE'
for x in a:
    if (int(f'97531{x}19', 15) + int(f'3{x}519', 15)) % 11 == 0:
        print(x, int(x, 15) // 11)

print(3 // 11)