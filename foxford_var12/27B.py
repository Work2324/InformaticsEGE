f = open('27B.txt')

m1, m2, m3 = [], [], []
for i in f:
    temp = list(map(float, i.split()))
    if ((temp[0] + 0.668117585879902)**2 + (temp[1] - 1.33366718014354)**2)**0.5 < 1.5720912136785356:
        m1.append(temp)
    elif ((temp[0] - 0.862295654841089)**2 + (temp[1] - 3.67170106454741)**2)**0.5 < 1.6801541477063033:
        m2.append(temp)
    else:
        m3.append(temp)

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

sm3 = 100000000000000
for i in range(len(m3)):
    sm = 0
    for k in range(len(m3)):
        sm += ((m3[i][0] -m3[k][0])**2 + (m3[i][1] - m3[k][1])**2)**0.5
    if sm < sm3:
        sm3 = sm
        t3 = i
        
print(int(((m1[t1][0] + m2[t2][0] + m3[t3][0])/3) *10000), int(((m1[t1][1] + m2[t2][1] + m3[t3][1])/2) * 10000))
