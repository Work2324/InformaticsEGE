for n in range(1,  10000):
    s = bin(n)[2:]
    if sum(list(int(i) for i in s)) % 2 == 0:
        s = '10' + s[:-1] + '1'
    else:
        s = '1' + s[:-2] + '11'

    if int(s, 2) >= 85:
        print(n, bin(n), s)
        break
