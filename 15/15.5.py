def f(x, y, a):
    return ((a < x) or (x ** 2 - 7 * x + 10 > 0)) and ((a >= y) or (y ** 2 + 7 * y + 12 > 0))

k = 0
for a in range(-100, 101):
    fl = True
    for x in range(-100, 101):
        for y in range(-100, 101):
            if not(f(x, y, a)):
                fl = False
                break
        if fl == False:
            break
    if fl:
        k += 1

print(k)