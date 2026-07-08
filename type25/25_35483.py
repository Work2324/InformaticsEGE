from math import *

for i in range (35000000, 40000001):
    t = 0
    temp = int(sqrt(i))
    for k in range(1, temp + 1):
        if i % k == 0:
            if k % 2 == 1:
                t += 1
            if (int(i / k) % 2) == 1 and (k ** 2) != i:
                t += 1
            

    if t == 5:
        print(i)
