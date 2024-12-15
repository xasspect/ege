from turtle import *
k = 10
left(90)
tracer(0)
pendown()
begin_fill()
for x in range(4):
    forward(8*k)
    right(90)
for y in range(3):
    forward(12*k)
    right(120)
end_fill()

canvas = getcanvas()
for x in range(-200, 200):
    for y in range(-200, 200):

