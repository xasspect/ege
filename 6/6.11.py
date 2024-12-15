from turtle import *
k = 13
left(90)
tracer(0)
screensize(1000, 1000)
for x in range(2):
    fd(23 * k)
    lt(90)
    backward(27 * k)
    lt(90)
up()
backward(5 * k)
rt(90)
fd(11 * k)
lt(90)

down()
for x in range(2):
    fd(26 * k)
    rt(90)
    fd(32* k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()










