from turtle import *
speed(20)
k = 10

for i in range(5):
    circle(5 * k, 180)
    seth(90)
    circle(5 * k, 180)
    seth(180)
    circle(5 * k, 180)
    seth(270)
    circle(5 * k, 180)
    seth(0)


penup()
for x in range(- 16, 11):
    for y in range(-8, 17):
        goto(x * k, y * k)
        dot(3, 'red')
