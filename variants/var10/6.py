from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for x in range(2):
    fd(7 * k)
    rt(90)
    fd(18 * k)
    rt(90)
up()
backward(-2 * k)
rt(90)
fd(9 * k)
lt(90)
down()
for x in range(3):
    fd(8 * k)
    rt(120)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'blue')
done()