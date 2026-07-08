def fun(s, c, end):
    if s >= 149 or c > end:
        if c % 2 == end % 2: return 1
        else: return 0

    h1 = fun(s + 1, c + 1, end)
    h2 = fun(s * 2, c + 1, end)

    if (c + 1) % 2 == end % 2:
        return h1 or h2
    else:
        return h1 and h2

for s in range(1, 149):
    if fun(s, 0, 2) == False and fun(s, 0, 4) == True:
        print(s)
