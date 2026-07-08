def f(n):
    for i in range(3):
        if n % 2 == 0:
            b = n // 2
            temp = ''
            for k in str(b):
                temp += k + ' '
                
            if sum(map(int, temp.split())) % 2 == 0:
                n = b
            else:
                return False
        else:
            b = (n - 1) // 2
            temp = ''
            for k in str(b):
                temp += k + ' '
                
            if sum(map(int, temp.split())) % 2 == 1:
                n = b
            else:
                return False

    return True


#main

t = 0
for i in range(123456789, 1987654322):
        if f(i):
            t += 1
            

print(t)
