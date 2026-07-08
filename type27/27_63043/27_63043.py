f = open('27-B.txt')
k = int(f.readline())
n = int(f.readline())
m =[]
for i in f:
    m.append(int(i))

mx = -1000000000
for i in range(n - 3 * k - 1):
    if (m[i] + m[i + 3 * k]) > mx:
        mx = m[i] + m[i + 3 * k]
        j = i

mx = -1000000000
for i in range(n - 1):
    if m[i] > mx and i != j and i != (j + 3 * k):
        mx =m[i]
        l = i

print(m[j] + m[j + 3 * k] + m[l])
