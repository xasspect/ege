k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    a.sort()
    s = [a[0], a[-1]]
    sa = sum(s) / len(s)
    if sa in a:
        k += 1
print(k)