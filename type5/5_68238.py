ans = []
for i in range(100, 100000):
    m =[]
    for k in range(0, len(str(i))-2):
        m.append(int(str(i)[k] + str(i)[k+1] + str(i)[k+2]))

    r = max(m) - min(m)

    if r == 415:
        print(i)
