f = open('17.txt')
f = list(map(int, f.read().split()))

t = 0
maxx = 0
for i in range(len(f) - 2):
    if f[i] ** 2 < f[i + 1] ** 2 + f[i + 2] ** 2:
        if f[i + 1] ** 2 < f[i] ** 2 + f[i + 2] ** 2:
            if f[i + 2] ** 2 < f[i + 1] ** 2 + f[i] ** 2:
                maxx = max(maxx, f[i] + f[i + 1] + f[i + 2])
                t += 1


print(t, maxx)
