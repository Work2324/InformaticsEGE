f = open('27-B.txt')
n = int(f.readline())

sm = 0
A = [0] * 999
t = 0
for i in f:
    b = int(i)
    sm += b
    if sm % 999 == 0:
        t += 1
    t += A[sm % 999]
    A[sm % 999] += 1

print(t)
