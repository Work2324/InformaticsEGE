f = open('27A.txt')

m1, m2 = [], []
for i in f:
    temp = list(map(float, i.split()))
    if temp[1] <= 1.85:
        m2.append(temp)
    else:
        m1.append(temp)

sm1 = 100000000000
for i in range(len(m1)):
    sm = 0
    for k in range(len(m1)):
        sm += ((m1[i][0] -m1[k][0])**2 + (m1[i][1] - m1[k][1])**2)**0.5
    if sm < sm1:
        sm1 = sm
        t1 = i

sm2 = 100000000000000
for i in range(len(m2)):
    sm = 0
    for k in range(len(m2)):
        sm += ((m2[i][0] -m2[k][0])**2 + (m2[i][1] - m2[k][1])**2)**0.5
    if sm < sm2:
        sm2 = sm
        t2 = i

print(int(((m1[t1][0] + m2[t2][0])/2) *10000), int(((m1[t1][1] + m2[t2][1])/2) * 10000))
