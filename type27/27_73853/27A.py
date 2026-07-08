f = open('27A.txt')
m = []
for i in f:
    m.append(list(map(float, i.split())))

m1, m2, m3 = [], [], []
for i in m:
    if i[1] <= 2.4:
        m1.append(i)
    elif i[1] > 2.4 and i[1] < 5.4:
        m2.append(i)
    else:
        m3.append(i)

d = {len(m1) : m1, len(m2) : m2, len(m3) : m3}
#print(d.keys())
d.pop(min(len(m1), len(m2), len(m3)))
#print(d.keys())
A = list(d.values())


s = []
for i in A:
    p = []
    for k in range(len(i)):
        sm = 0
        for j in range(len(i)):
                sm += ((i[k][0] - i[j][0])**2 + (i[k][1] - i[j][1])**2)**0.5
        p.append(sm)
    s.append(p.index(min(p)))

#print(A[0][25], A[1][215])
ans = 0
for i in range(len(A)):
    mx = 0
    for k in range(len(A[i])):
        temp = ((A[i][s[i]][0] - A[i][k][0])**2 + (A[i][s[i]][1] - A[i][k][1])**2)**0.5
        if  temp > mx:
                   mx = temp
    ans += mx

print(ans/len(A))
#не решено
