t = 0
for x in range(0, 18):
    for y in range(-6, 17):
        if (y <= min(x/(3**0.5) + 10, (-1) * x/(3**0.5) + 20) and y >= max((-1)*x/(3**0.5), x/(3**0.5) - 10)):
            t += 1


print(t)


#PERFECT!!!
