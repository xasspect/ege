from turtle import *
k = 30
left(90)
tracer(0)
screensize(1000, 1000)
for x in range(16):
    fd(10 * k)
    rt(120)
    fd(10 * k)
    rt(60)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()