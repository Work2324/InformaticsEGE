f = open("17_76232.txt")
m = []
mn = 1000000
for i in f:
    k = int(i)
    m.append(int(i))
    if (str(abs(int(i)))[0] == '5')  and (len(str(abs(int(i)))) == 3) and int(i) < mn:
        mn = int(i)

print(mn)

mx = -1000000
t = 0
for i in range(len(m)-2):
    if (str(m[i])[-1] == '4') + (str(m[i + 1])[-1] == '4') + (str(m[i + 2])[-1] == '4')  == 1:
        if abs(m[i] + m[i + 1] + m[i + 2]) % mn != 0:
            mx = max(mx, m[i] + m[i + 1] + m[i + 2])
            t += 1


print(t, mx)
