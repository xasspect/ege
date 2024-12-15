from turtle import *
k = 1
left(90)
tracer(0)
screensize(1000, 1000)
for x in range(100):
    lt(45)
    for i in range(8):
        fd(50 * k)
        rt(45)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'blue')
done()