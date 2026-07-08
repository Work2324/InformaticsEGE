f = open('24_demo.txt')
f = f.read()
dl = len(f)

temp = 0
temp2 = 0
maxx = 0
i = 0
while i < dl - 2:
    temp2 = temp
    
    if f[i] + f[i + 1] + f[i + 2] == 'XYZ':
        temp += 3
        i += 2
        
    elif f[i] + f[i + 1] == 'XY':
        temp += 2
        i += 1
        maxx = max(maxx, temp)
        temp = 0
        
    elif f[i] == 'X':
        temp += 1
        maxx = max(maxx, temp)
        temp = 0
        
    if temp2 == temp and temp2 != 0:
        maxx = max(maxx, temp)
        temp = 0
        
    i += 1

print(maxx)
            
    
