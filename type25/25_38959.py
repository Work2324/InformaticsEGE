i = 200000001
t = 0
m = []
s = 1
while t < 5:
    for k in range(2, i):
        if i % k == 0:
            m.append(k)
        if len(m) >= 5:
            break
    
    for k in m:
        s *= k

    if len(m) < 5:
        s = 0

    if s < i and s != 0:
        print(s)
        t += 1

    m = []
    s = 1
    i += 1
