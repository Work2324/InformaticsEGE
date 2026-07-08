s = 'ВИКОРТ'
t = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        temp = i1 + i2 + i3 + i4 + i5 + i6
                        fl = True
                        for k in temp:
                            if temp.count(k) != 1:
                                fl = False
                                
                        if fl == True:
                            t += 1
                            if t == 266:
                                print(temp)
