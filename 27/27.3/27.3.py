with open('27a.txt') as f:
    f.readline()
    c1, c2 = [], []
    for i in f:
        x, y, h = map(float, i.replace(',', '.').split())
        if 0 <= x <= 150 and 125 <= y <= 300:
            c1.append((x, y, h))
        if 325 <= x <= 500 and 225 <= y <= 400:
            c2.append((x, y, h))

def centroid(cluster):
    x_centr, y_centr, minim = 0, 0, 10 ** 100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1, h = cluster[i]
            x2, y2, h = cluster[j]
            res += (((x2 - x1) * h) ** 2 + ((y2 - y1) * h) ** 2) ** 0.5
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y2
    return x_centr, y_centr

x1, y1 = centroid(c1)
x2, y2 = centroid(c2)
print((x1 + x2) / 2 * 100000, (y1 + y2) / 2 * 100000)