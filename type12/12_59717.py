def f(n):
    sm = 0
    for k in n:
        sm += int(k)

    return sm


for i in range(3, 10001):
    s = '5' + '2' * i
    t = 1
    while t == 1:
        t = 0
        if '52' in s:
            s = s.replace('52', '11', 1)
            t = 1
        if '2222' in s:
            s = s.replace('2222', '5', 1)
            t = 1
        if '1122' in s:
            s = s.replace('1122', '25', 1)
            t = 1

    if f(s) == 64:
        print(i)
        break
