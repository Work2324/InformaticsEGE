f = open('17_63033.txt')
m = []
mx = 0
for i in f:
    m.append(int(i))
    if int(i) % 1000 == 123:
        mx = max(mx, int(i))

t = 0
mxx = 0
for i in range(len(m) - 2):
    if ((m[i] % 3 == 0)  + (m[i + 1] % 3 == 0) + (m[i + 2] % 3 == 0)) == 1:
        if (len(str(m[i])) == 5) + (len(str(m[i + 1])) == 5) + (len(str(m[i  + 2])) == 5) >= 2:
            if (m[i] + m[i  + 1] + m[i + 2]) > mx:
                t += 1
                mxx = max(mxx, (m[i] + m[i  + 1] + m[i + 2]))

print(t, mxx)
                
