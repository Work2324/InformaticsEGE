f = open("17_37337.txt")
A = []
for i in f:
    A.append(int(i))

j = 0
mx = 0

for i in range(len(A)-1):
    for k in range(i + 1, len(A)):
        if (A[i] % 160 != A[k] % 160) and (A[i] % 7 == 0 or A[k] % 7 == 0):
            j += 1
            if A[i] + A[k] > mx:
                mx = A[i] + A[k]


print(j, mx)
