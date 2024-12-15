from turtle import *
k = 20
left(90)
tracer(0)
screensize(10000, 10000)
for x in range(5):
    fd(8 * k)
    rt(90)
    fd(11 * k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')

done()
