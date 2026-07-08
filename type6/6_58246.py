t = 0
for x in range(-42, 3):
    for y in range(-4, 8):
        if y > -2 and y < 0 and x > -40 and x < 0:
            t += 1
        if x > -40 and x < -30 and y >= 0:
            if (x + 35)**2 + (y)**2 < 25:
                t += 1
        if x > -30 and x < -20 and y >= 0:
            if (x + 25)**2 + (y)**2 < 25:
                t += 1
        if x > -20 and x < -10 and y >= 0:
            if (x + 15)**2 + (y)**2 < 25:
                t += 1
        if x > -10 and x < 0 and y >= 0:
            if (x + 5)**2 + (y)**2 < 25:
                t += 1

print(t)
