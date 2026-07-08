f = open('17_72575.txt')
m = []
for i in f:
    m.append(int(i))

mn = min(m) % 3
mx = max(m) % 7
t = 0
mxx = 0 
for i in range(len(m) - 1):
    if m[i] % 3 == mn or m[i+1] % 3 == mn:
        if  m[i] % 7 == mx or m[i+1] % 7 == mx:
            t += 1
            mxx = max(m[i] + m[i + 1], mxx)

print(t, mxx)
