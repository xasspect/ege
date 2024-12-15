a = str(open('24.txt').readlines())
a = [x for x in a]


s = ['Q', 'R', 'W']
n = ['1', '2', '4']

for i in range(len(a) - 1):
    c = 0
    while (a[i] in s) and (a[i + 1] not in s):
        c += 1

    print(c)



