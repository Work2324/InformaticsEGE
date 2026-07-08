t = 0
for x in range(-6, 17):
    for y in range(-6, 17):
        if (x**2 + (y - 5)**2 < 25) or x > 0:
            if ((x - 5)**2 + (y - 10)**2 < 25) or y < 10:
                if ((x - 10)**2 + (y - 5)**2 < 25) or x < 10:
                    if ((x - 5)**2 + y**2 < 25) or y > 0:
                        t += 1

print(t)
