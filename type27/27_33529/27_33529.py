f = open('27-B.txt')
n = f.readline()
m = []
for i in f:
    m.append(list(map(int, i.split())))
    m[-1].append(abs(m[-1][0]-m[-1][1]))

mn = 100000000000
sm = 0
ch = 0
nech = 0
for i in range(len(m)):
    temp = max(m[i][0], m[i][1])
    sm += temp
    if temp % 2 == 0: ch += 1
    else: nech += 1
    if m[i][-1] < mn and m[i][-1] % 2 == 1:
        mn = m[i][-1]

print(sm, ch, nech)
sm = sm - mn * (sm % 2 != (nech - ch > 0))
print(sm)

