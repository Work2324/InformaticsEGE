f = open('24_27691.txt').read()
t = 0
mx = 0
for i in f:
    if i == 'A':
        t += 1
    else:
        mx = max(mx, t)
        t = 0

print(mx)
