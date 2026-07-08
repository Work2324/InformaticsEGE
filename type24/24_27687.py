f = open("24_27687.txt").read()
mx = 0
t = 0
for i in f:
    if i == "Y":
        t += 1
    else:
        if mx < t:
            mx = t
        t = 0

print(mx)
        
