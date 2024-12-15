s = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
s = str(s)
print(s)
for x in range(len(s) - 1):
    if s[x + 1] == '0':
        print(s[x], s[x + 1])
