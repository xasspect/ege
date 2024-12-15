from turtle import *
k = 25
left(90)
tracer(0)
screensize(10000, 10000)
for x in range(9):
    fd(22 * k)
    rt(90)
    fd(6 * k)
    rt(90)
up()
fd(1 * k)
rt(90)
fd(5 * k)
lt(90)
down()
for x in range(9):
    fd(53 * k)
    rt(90)
    fd(75 * k)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'blue')
done()