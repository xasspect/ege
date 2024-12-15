from turtle import *
k = 20
tracer(0)
left(90)
screensize(1000, 1000)
for x in range(6):
    fd(5 * k)
    rt(60)
up()
fd(5* k)
rt(90)
down()
for x in range(2):
    fd(15 * k)
    rt(90)
    fd(5 * k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()
