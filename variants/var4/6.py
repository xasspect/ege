from turtle import *
k = 30
left(90)
tracer(0)
screensize(1000, 1000)
for x in range(6):
    fd(10 * k)
    rt(90)
fd(2 * k)
rt(90)
for x in range(2):
    fd(15* k)
    rt(90)
    fd(4 * k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()

