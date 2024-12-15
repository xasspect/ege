k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    for i in range(len(a) - 2):
        x1 = a[i]
        x2 = a[i + 1]
        x3 = a[i + 2]
        if x1 == 60 and x2 == 60 and x3 == 60:
            k += 1
print(k)