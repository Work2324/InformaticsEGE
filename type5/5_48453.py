def fun(s):
    ans = ''
    for i in s:
        ans += str((int(i) + 1) % 2)

    ans = ans[ans.find('1'):]
    return ans

        
for i in range(1, 10000000):
    b = bin(i)[2:]
    if i - int(fun(b), 2) == 979:
        print(i)
        break
    
