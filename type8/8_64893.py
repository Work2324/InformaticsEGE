t = 0
for i in range(100000000000,999999999999):
    s = str(i)
    fl = True
    for k in range(0, 11):
        if int(s[k] + s[k+1]) % 2 == 0:
            if int(s[k+1]) <= int(s[k]):
                fl = False
        else:
            if int(s[k]) <= int(s[k+1]):
                fl = False

    if fl:
        t += 1

print(t)
