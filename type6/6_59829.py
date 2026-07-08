from turtle import *
k = 10
for i in range(2):
    forward(9 * k)
    right(90)
    forward(15 * k)
    right(90)

penup()
fd(12 * k)
right(90)
pendown()

for i in range(2):
    fd(6 * k)
    right(90)
    fd(12 * k)
    right(90)

penup()

for  x in range(-8, 15):
    for y in range(-20, 6):
        goto(x * k, y * k)
        dot(3)
