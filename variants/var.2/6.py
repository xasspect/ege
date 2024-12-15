from turtle import *
k = 30
left(90)
tracer(0)
screensize(1000, 1000)
for i in range(2):
    rt(120)
    fd(7 * k)
rt(300)
for j in range(2):
    rt(120)
    fd(7 * k)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()
