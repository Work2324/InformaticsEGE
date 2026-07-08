def funct(n):
    if n in l:
        return l[n]
    else:
        if n < 15:
            return n
        else:
            return funct(n % 15) * funct(n // 15)

l = dict()
t = 3**40
j = 0
for i in range(1, t):
    l[i] = funct(i)
    if l[i] == 7560:
        j += 1

#nope
