def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
        
    return s

ans = []
for i in range(4, 1000):
    s = f(i)
    #print(i, s, end = " ")
    if i % 3 == 0:
        s += s[-2:]
    else:
        sm = sum(map(int, s))
        sm *= 3
        s += f(sm)

    #print(s, int(s, 3))
    temp = int(s, 3)
    if temp >= 910:
        #print(i, temp)
        ans.append(temp)

print(min(ans))
