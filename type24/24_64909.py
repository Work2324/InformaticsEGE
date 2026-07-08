f = open("1.txt").read()
alf = "UVWXYZ"
s = ""
m = {"U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}
mx = 0
for i in f:
    if i in alf:
        s = s + i
        m[i] += 1
        if m[i] > 100:
            print(s)
            ind = s.find(i) + 1
            s[ind:]
            print(s)
            m = {"U" : s.count("U"), "V" : s.count("V"), "W" : s.count("W"), "X" : s.count("X"), "Y" : s.count("Y"), "Z" : s.count("Z")}
            print(m)
        mx = max(mx, len(s))
        
print(mx)

#да оно тебе не надо










#БЕГИ ОТ СЮДА!!!!
