def fun(s, c, end):
    if s <= 26005 or c > end:
        if c % 2 == end % 2: return 1
        else: return 0

    h1 = fun(s - 2, c + 1, end)
    h2 = fun(s - 7, c + 1, end)
    h3 = fun(s // 3, c + 1, end)

    if (c + 1) % 2 == end % 2:
        return h1 or h2 or h3
    else:
        return h1 and h2 and h3

ans = 0
for i in range(26006, 1000000):
    if fun(i, 0, 2):
        ans = i

print(ans)
