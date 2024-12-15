with open('27a.txt') as f:
    f.readline()
    c1, c2 = [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -4 <= x <= 6 and -4 <= y <= 5:
            c1.append((x, y))
        if 6 <= x <= 14 and 3 <= y < 12:
            c2.append((x, y))




def centroid(cluster):
    x_centr, y_centr, minim = 0, 0, 10 ** 100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

x1, y1 = centroid(c1)
x2, y2 = centroid(c2)
print((x1 + x2) / 2 * 100, (y1 + y2) / 2 * 100)

