f = open('27-B_demo.txt')
n = f.readline()
m = []
for i in f:
    m.append(list(map(int, i.split())))
    m[-1].append(abs(m[-1][0] - m[-1][1]))
    
sm = 0
for i in m:
    sm += max(i[0], i[1])

mn = 100000000
for i in m:
    if i[2] < mn and (sm - i[2])  % 3 != 0:
        mn = i[2]
            
sm -= mn

print(sm)
    
#nice;)
