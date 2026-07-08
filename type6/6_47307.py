t = 0
for x in range(-1, 11):
    for y in range(-1, 17):
        if x > 0 and x < 5*3**0.5:
            if y < 1 / (3**0.5) * x + 10 and y > 1/(3**0.5)*x:
                t += 1

print(t)


'''
from turtle import *
k = 10
left(90)

for i in range(4):
    fd(10 * k)
    right(60)
    fd(10 * k)
    right(120)

penup()

for x in range(-1, 11):
    for y in range(-1, 17):
        goto(x * k, y * k)
        dot()
'''
