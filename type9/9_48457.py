f = open('9_48457.txt')
t = 0
for i in f:
    m = list(map(int, i.split()))

    d = {}
    for k in m:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

    nepov = []
    pov = []
    for k in d:
        if d[k] == 1:
            nepov.append(k)
        if d[k] == 2:
            pov.append(k)

    if len(pov) == 2 and len(nepov) == 2:
        if sum(pov) > sum(nepov):
            t += 1

print(t)
