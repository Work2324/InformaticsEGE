def fn(s1, s2, c, end):
    if s1+s2 > 40 or c > end:
        if c % 2 == end % 2: return True
        else: return False
        
    if s1 > s2:
        h1 = fn(s1  + 1, s2, c + 1, end)
        h2 = fn(s1  + 2, s2, c + 1, end)
        h3 = fn(s1  + 3, s2, c + 1, end)
        h4 = fn(s1, s2 * 2, c + 1, end)
    elif s1 < s2:
        h1 = fn(s1, s2 + 1, c + 1, end)
        h2 = fn(s1, s2  + 2, c + 1, end)
        h3 = fn(s1, s2 + 3, c + 1, end)
        h4 = fn(s1 * 2, s2, c + 1, end)
    else:
        h1 = fn(s1  + 1, s2, c + 1, end)
        h2 = fn(s1  + 2, s2, c + 1, end)
        h3 = fn(s1  + 3, s2, c + 1, end)
        h4 = (c + 1) % 2

    if (c + 1) % 2 == end % 2:
        return h1 or h2 or h3 or h3 or h4
    else:
        return h1 and h2 and h3 and h4

for i in range(1, 23):
    if fn(17, i, 0, 4) == True and fn(17, i, 0, 2) == False:
        print(i)
