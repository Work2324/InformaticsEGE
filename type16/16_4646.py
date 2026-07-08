#import sys
#sys.setrecursionlimit(1000000000)

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return f(n-1)*n + f(n-2)*(n-1)
    else:
        print("error")
        return -1

print(f(5))
    
