from turtle import *
k = 10
tracer(0)
screensize(1000, 1000)
for x in range(9):
    fd(18 * k)
    rt(72)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()