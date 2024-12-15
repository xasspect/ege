with open('27a.txt') as f:
    f.readline()
    c1, c2, c3, c4, c5 = [], [], [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 4 <= x <= 7 and 1 <= y <= 4:
            c1.append((x, y))
        if 5 <= x <= 8 and 6 <= y <= 9:
            c2.append((x, y))
        if 8 <= x <= 11 and 10 <= y <= 13:
            c3.append((x, y))
        if 8 <= x <= 11 and 14 <= y <= 17:
            c4.append((x, y))
        if 13 <= x <= 16 and -1 <= y <= 2:
            c5.append((x, y))


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
x3, y3 = centroid(c3)
x4, y4 = centroid(c4)
x5, y5 = centroid(c5)
print((x1 + x2 + x3 + x4 + x5) / 5 * 10000, (y1 + y2 + y3 + y4 + y5) / 5 * 10000)
