from turtle import *
k = 20
lt(90)
tracer(0)
screensize(10000, 10000)
for x1 in range(2):
    fd(11 * k)
    rt(90)
    fd(17 * k)
    rt(90)
up()
fd(7 * k)
lt(90)
backward(1 * k)
rt(90)
down()
for x2 in range(2):
    fd(15 * k)
    rt(90)
    fd(7 * k)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3, 'blue')

update()
done()