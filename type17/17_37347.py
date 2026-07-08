f = open('17_37347.txt')
m = []
for i in f:
    m.append(int(i))

mx = 0
t = 0
for i in range(len(m) - 1):
    for k in range(i + 1, len(m)):
        if m[i] * m[k] % 14 != 0:
            mx = max(mx, m[i] + m[k])
            t += 1

print(t, mx)
