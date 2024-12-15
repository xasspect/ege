from turtle import *
print(25 + 16)
k = 20
left(90)
tracer(0)
screensize(1000, 1000)
rt(120)
for x in range(8):
    fd(4 * k)
    rt(60)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'blue')
done()
