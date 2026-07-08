f = open('17_37341.txt')
A = []
for i in f:
    A.append(int(i))

mas = []
for i in range(len(A) - 1):
    for k in range(i + 1, len(A)):
        if (max(k, i) - min(k, i)) % 2 == 0 and (k % 19 == 0 or i % 19 == 0):
            mas.append(k + i)

print(len(mas), max(mas))
