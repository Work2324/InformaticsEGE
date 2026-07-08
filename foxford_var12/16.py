from functools import *


@cache
def fun(n):
    if n == 1:
        return 5
    else:
        return 2 * n + fun(n - 1)

for i in range(1, 2048):
    fun(i)
    
print(fun(2048) - fun(1024))
