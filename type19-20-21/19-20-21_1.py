def fun(s, c, end):
    if s >= 50 or c > end:
        if s <= 119 or c > end:
            if c % 2 == end % 2: return 1
            else: return 0
        else:
            if c % 2 == end % 2: return 0
            else: return 1
    
    h1 = fun(s + 2, c + 1, end)
    h2 = fun(s * 3, c + 1, end)

    if (c + 1) % 2 == end % 2:
        return h1 or h2
    else:
        return h1 and h2


for i in range(1, 50):
    if fun(i, 0, 2) == False and fun(i, 0, 4) == True:
        print(i)
