from turtle import *
k = 20
for i in range(4):
    fd(8 * k)
    right(150)
    fd(8 * k)
    right(30)

penup()
for x in range(-8, 9):
    for y in range(-8, 9):
        goto(x * k, y * k)
        dot()
