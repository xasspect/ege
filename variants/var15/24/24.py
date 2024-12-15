a = list(open('24.txt'))[0]
k = 0
for i in range(len(a) - 2):
    x1 = a[i]
    x2 = a[i + 1]
    x3 = a[i + 2]
    if x1 + x2 + x3 == 'abc':
        k += 1
print(k)
