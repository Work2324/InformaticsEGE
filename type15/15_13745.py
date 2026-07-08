ans = []
for A in range (901):
    fl = True
    for x in range (31):
        for y in range (31):
            if ((x > 9) or (x**2 <= A)) and ((y**2 > A) or (y <= 9)) == 0:
                fl = False
                break

    if fl == True:
        ans.append(A)


print(max(ans))
                
