from turtle import *
k = 20
Screen().tracer(0)
for i in range(0, 6):
    fd(10 * k)
    right(60)

penup()
for x in range(-12, 20):
    for y in range(-20, 11):
        goto(x * k, y * k)
        dot(size = 2)

#фигня решение:(
