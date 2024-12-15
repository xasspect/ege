from turtle import *
k = 10
left(90)
tracer(0)
pendown()
begin_fill()
for i in range(2):

    forward(7*k)
    right(60)
end_fill()
penup()
forward(7*k)
right(60)
pendown()

for j in range(2):
    forward(5*k)
    right(120)
    forward(10*k)
    right(60)



penup()

canvas = getcanvas()
count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        # print(canvas.find_overlapping(x * k, y * k, x * k, y * k))
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            count += 1

print(count)

done()






