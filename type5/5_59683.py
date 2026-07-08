def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2

    return(s)
mx = 0
for i in range(1, 1000):
    s = f(i)
    if i % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + str(f((i % 3) * 3))

    temp = int(s, 2)
    if temp <= 170:
        if temp > mx:
            mx = temp

print(mx)
