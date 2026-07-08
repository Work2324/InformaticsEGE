f = open("17_37336.txt")
k = int(f.readline())
j = 0
mx = -10000000
for i in f:
    if k % 3 == 0 or int(i) % 3 == 0:
        j += 1
        if int(i) + k > mx:
            mx = int(i) + k
    k = int(i)


print(j, mx)
