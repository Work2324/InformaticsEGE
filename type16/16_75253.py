#import sys
#sys.setrecursionlimit(1000000000)

def f(n):
    if n == 0:
        return 0
    elif n > 0 and n%4 < 2:
        return f(n//4) + n%4
    elif n > 0 and n%4 >= 2:
        return f(n//4) + n%4 -1
    else:
        print("error")
        return -1

for i in range(100000001):
    if f(i) == 27 and f(i+1) == 16:
        print(i)
        break

print('hi')
    
