with open('27b.txt') as f:
    f.readline()
    c1, c2, c3 = [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -3 <= x <= 0.8 and -1 <= y <= 2.9:
            c1.append((x, y))
        if 0.2 <= x <= 4 and 2 <= y <= 6:
            c2.append((x, y))
        if 0.3 <= x <= 4 and -4 <= y <= -0.2:
            c3.append((x, y))

def centroid(cluster):
    x_centr, y_centr, minim = 0, 0, 10 ** 100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

x1, y1 = centroid(c1)
x2, y2 = centroid(c2)
x3, y3 = centroid(c3)
print((x1 + x2 + x3) / 3 * 100000, (y1 + y2 + y3) / 3 * 100000)
# a = 43744, -47901
# b =



