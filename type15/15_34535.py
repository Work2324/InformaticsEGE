A = []
for l in range(4, 51):
    for r in range(l + 1, 52):
        f = 1
        for i in range(4, 52):
            f = (((l<=i<=r) or (10<=i<=40)) or ((5<=i<=15) <= (35<=i<=50))) * f
            
        if f:
            A.append(r - l)

print(min(A))
