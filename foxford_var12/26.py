f = open('26.txt')
n = f.readline()

m = []
A = []
for i in f:
    m.append(int(i))

for i in range(len(m)):
    fl = False
    for k in range(len(A)):
        if A[k][0] == m[i]:
            A[k][1] += 1
            fl = True
            break
    if fl == False:
        A.append([m[i], 1])

sm = 0
t = 0
for i in A:
    sm += i[0] * (i[1] - i[1] // 3)
    t += i[1] // 3
print(sm, t)
