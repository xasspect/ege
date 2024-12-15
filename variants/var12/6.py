from turtle import *
k = 30
lt(90)
tracer(0)
screensize(10000, 10000)
rt(270)
for x in range(8):
    fd(10 * k)
    rt(45)
    fd(10 * k)
    rt(135)

for x in range(4):
    fd(4 * k)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'blue')
done()