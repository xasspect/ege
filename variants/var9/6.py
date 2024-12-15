from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)

for x in range(7):
    fd(20 * k)
    rt(240)
    fd(10 * k)
    rt(240)
    fd(20 * k)
    rt(120)
    fd(10 * k)
    rt(120)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'blue')
done()