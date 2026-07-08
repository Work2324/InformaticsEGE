def fun(s1, s2, c, end):
    if s1 + s2 >= 75 or c > end:
        if c % 2 == end % 2: return 1
        else: return 0

    h1 = fun(s1 + 1, s2, c + 1, end)
    h2 = fun(s1, s2 + 1, c + 1, end)
    h3 = fun(s1 + s2, s2, c + 1, end)
    h4 = fun(s1, s2 + s1, c + 1, end)

    if (c + 1) % 2 == end % 2:
        return h1 or h2 or h3 or h4
    else:
        return h1 and h2 and h3 and h4 #если Петя неудачник: and -> or

#19
for i in range(1, 68):
    if fun(7, i, 0, 2):
        print(i)

#20
for i in range(1, 68):
    if fun(7, i, 0, 1) == False and fun(7, i, 0 , 3) == True:
        print(i)

#21
for i in range(1, 68):
    if fun(7, i, 0, 2) == False and fun(7, i, 0 , 4) == True:
        print(i)
