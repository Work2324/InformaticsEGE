f = open('17_39763.txt')
k = int(f.readline())
j = int(f.readline())
mx = 0
t = 0
for i in f:
    if (int(i)**2 + k**2 > j**2) and (int(i)**2 + j**2 > k**2) and (k**2 + j**2 > int(i)**2):
        t += 1
        if int(i) + k + j > mx:
            mx = int(i) + k + j

    k = j
    j = int(i)

print(t, mx)
