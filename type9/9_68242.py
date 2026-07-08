def funct(m1, m2, m3):
    t = 0
    for i in range(len(m2)):
        if m2.count(m2[i]) == 1:
            if m1 == None:
                if i == 0:
                    s = list({m2[i], m2[i + 1], m3[i], m3[i + 1]})
                    if max(s) > m2[i]:
                        t += 1
                elif i == len(m2) - 1:
                    s = list({m2[i - 1], m2[i], m3[i - 1], m3[i]})
                    if max(s) > m2[i]:
                        t += 1
                else:
                    s = list({m2[i - 1], m2[i], m2[i + 1], m3[i - 1], m3[i], m3[i + 1]})
                    if max(s) > m2[i]:
                        t += 1      
            elif m3 == None:
                if i == 0:
                    s = list({m1[i], m1[i + 1], m2[i], m2[i + 1]})
                    if max(s) > m2[i]:
                        t += 1
                elif i == len(m2) - 1:
                    s = list({m1[i - 1], m1[i], m2[i - 1], m2[i]})
                    if max(s) > m2[i]:
                        t += 1
                else:
                    s = list({m1[i - 1], m1[i], m1[i + 1], m2[i - 1], m2[i], m2[i + 1]})
                    if max(s) > m2[i]:
                        t += 1
            else:
                if i == 0:
                    s = list({m1[i], m1[i + 1], m2[i], m2[i + 1], m3[i], m3[i + 1]})
                    if max(s) > m2[i]:
                        t += 1
                elif i == len(m2) - 1:
                    s = list({m1[i - 1], m1[i], m2[i - 1], m2[i], m3[i - 1], m3[i]})
                    if max(s) > m2[i]:
                        t += 1
                else:
                    s = list({m1[i - 1], m1[i], m1[i + 1], m2[i - 1], m2[i], m2[i + 1], m3[i - 1], m3[i], m3[i + 1]})
                    if max(s) > m2[i]:
                        t += 1

    return t




f = open('9_68242.txt')
A = []
for i in f:
    m = list(map(int, i.split()))
    A.append(m)

t = 0
for i in range(len(A)):
    m2 = A[i]
    fl = False
    if i == 0:
        m1 = None
        m3 = A[i + 1]
        if funct(m1, m2, m3) >= 3:
            fl = True
    elif i == len(A) - 1:
        m1 = A[i - 1]
        m3 = None
        if funct(m1, m2, m3) >= 3:
            fl = True
    else:
        m1 = A[i - 1]
        m3 = A[i + 1]
        if funct(m1, m2, m3) >= 3:
            fl = True

    if fl:
        for k in m2:
            if m2.count(k) > 1:
                t += 1
                break


print(t)










            
