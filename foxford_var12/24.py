f = open('24.txt').read()

n = -1
t = 0
mx = 0
for i in range(len(f)):
    if n != -1:
        if i % 2 == n % 2:
            if f[i] in 'AE':
                t += 1
            else:
                #print(n, i, f[n-1:i+2])
                #input()
                mx = max(mx, t)
                t = 0
                n = -1
        else:
            if f[i] in 'BCD':
                t += 1
            else:
                #print(n, i, f[n:i])
                #input()
                mx = max(mx, t)
                t = 0
                n = -1
    else:
        if f[i] in 'AE':
            n = i
            t += 1

#не верно, пропускаем 1 пару
print(mx)
