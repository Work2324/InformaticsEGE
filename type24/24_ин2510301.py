def d(s):
    ans = ''
    t = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'T':
            t += 1
            
        if t < 63:
            ans = s[i] + ans

    return 'T' + ans
            



f = open('24_ин2510301.txt').read()
mn = 10000000000
s = ''
fl = False
for i in range(len(f)):
    if f[i] == 'T' and s == '':
        fl = True

    if fl == True:
        s += f[i]
        
    if f[i] in 'AEIOUY':
        if s.count('T') >= 63:
            mn = min(mn, len(d(s)))
        s = ''
        fl = False

print(mn)
