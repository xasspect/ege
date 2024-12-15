a = list(set(list(map(int, open('17.txt')))))

t = []
k = 0
for x in range(len(a) - 1):
    if a[x] % 3 == 0:
        if a[x] % 7 != 0:
            if a[x] % 17 != 0:
                if a[x] % 19 != 0:
                    if a[x] % 27 != 0:
                        k += 1
                        t.append(a[x])
print(k, max(t))