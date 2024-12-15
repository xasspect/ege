from turtle import *
k = 100
left(90)
tracer(0)
pendown()
begin_fill()
for i in range(2):
    forward(5*k)
    right(90)
    forward(10*k)
    right(90)
end_fill()
penup()

cnt = 0
canvas = getcanvas()

for x in range(-200, 200):
    for y in range(-200, 200):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
            cnt += 1
print(cnt)
done()
