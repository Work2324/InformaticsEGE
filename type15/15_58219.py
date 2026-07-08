ans = []
for A in range(8, 33):
    for x in range(11, 30):
        fl = True
        treyg1 = max(20, x) < ((x + 20 + 10) - max(20, x))
        treug2 = max(A, x) < ((A + 3 + x) - max(A, x))
        if ((treyg1 <= (not(max(x, 8) > 24))) == (not(treug2))) == 0:
            fl = False
            break
        
    if fl:
        ans.append(A)

print(max(ans))
