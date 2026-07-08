a = []
for y in range(0, 10):
    if int('1' + str(y) + '31246') % 1983 == 0:
        a.append(nt('1' + str(y) + '31246'))

for x in range(0, 1000):
    for y in range(0, 10):
        x1 = int('1' + str(y) + '3124' + str(x) + '6')
        x2 = int('1' + str(y) + '31240' + str(x) + '6')
        x3 = int('1' + str(y) + '312400' + str(x) + '6')

        if x1 <= 10**10:
            if x1 % 1983 == 0:
                a.append(x1)
        if x2 <= 10**10:
            if x2 % 1983 == 0:
                a.append(x2)
        if x3 <= 10**10:
            if x3 % 1983 == 0:
                a.append(x3)

a = sorted(a)

print(a[0], a[0] / 1983)
print(a[1], a[1] / 1983)
print(a)
