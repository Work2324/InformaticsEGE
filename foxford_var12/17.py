f = open('17.txt')
m = []
mn = 100000000
for i in f:
    m.append(int(i))
    if mn > int(i) and abs(int(i)) % 10 == 4:
        mn = int(i)

mn = abs(mn)

t = 0
mx = -1
for i in range(len(m)-1):
    if (abs(m[i]) % 10 == 4) + (abs(m[i + 1]) % 10 == 4) == 1:
        if (m[i] + m[i  + 1])**2 >= mn:
            mx = max(mx, (m[i] + m[i  + 1])**2)
            t += 1


print(t, mx)
