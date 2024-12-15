from turtle import *
k = 13
tracer(0)
left(90)
screensize(1000, 1000)
for x in range(4):
    fd(19 * k)
    rt(90)
    fd(30 * k)
    rt(90)
up()
fd(2 * k)
rt(90)
fd(8 * k)
lt(90)
down()
for x in range(4):
    fd(90 * k)
    rt(90)
    fd(97 * k)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'blue')
done()
print(17 * 22)