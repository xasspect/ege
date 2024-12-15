with open('27b.txt') as f:
    f.readline()
    c1, c2, c3, c4 = [], [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 5 <= x <= 12 and 15 <= y <= 23:
            c1.append((x, y))
        if 10 <= x <= 15 and 4 <= y <= 10:
            c2.append((x, y))
        if 15.5 <= x <= 23 and 5 <= y <= 12:
            c3.append((x, y))
        if 22 <= x <= 30 and 15 <= y <= 21:
            c4.append((x, y))




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
print((x1 + x2 + x3 + x4) / 4 * 10000, (y1 + y2 + y3 + y4) / 4 * 10000)