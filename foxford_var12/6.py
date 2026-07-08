from turtle import *
import turtle
k = 5
turtle.Screen().tracer(0)

for i in range(8):
    fd(12 * k)
    left(45)

penup()
left(90)
fd(23 * k)
pendown()

for i in range(4):
    fd(58 * k)
    right(90)

penup()
for x in range(-10, 40):
    for y in range(-20, 40):
        goto(x * k, y * k)
        dot(size = 2)

turtle.Screen().update()
