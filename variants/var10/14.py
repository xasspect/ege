s = '0123456789abcdefghi'

for x in s:
    x1 = int(f'a3{x}74', 19)
    x2 = int(f'{x}40846', 19)
    if (x1 + x2) % 9 == 0:
        print(int(x, 19) // 9)
