from turtle import *
k = 10
left(90)
tracer(0)
screensize(10000, 10000)
rt(45)
for x in range(10):
    rt(45)
    fd(203 * k)
    rt(45)
up()
backward(40 * k)
rt(45)
down()
for x in range(5):
    fd(20 * k)
    lt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()