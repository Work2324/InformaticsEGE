f = open('18_33190.txt')
m = []
for i in f:
    m.append(float(i))


sm = m[0]
mx = -100000
for i in range(1, len(m)):
    
    if abs(m[i-1] - m[i ]) <=10 and  sm>0:
        sm += m[i]
    else:
        mx = max(mx, sm)
        sm = m[i]

print(mx)
