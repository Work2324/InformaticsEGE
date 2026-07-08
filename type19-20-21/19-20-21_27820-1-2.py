def f(s, c, end):
    if s >= 42 or c > end:
        if c % 2 == end % 2:
            return 1
        else:
            return 0


    h1 = f(s + 1, c + 1, end)
    h2 = f(s + 2, c + 1, end)
    h3 = f(s * 2, c + 1, end)

    if (c + 1) % 2 == end % 2:
        return h1 or h2 or h3
    else:
        return h1 and h2 and h3

for s in range(1, 41):
    if f(s, 0, 2) == False and f(s, 0, 4) == True:
        print(s)
