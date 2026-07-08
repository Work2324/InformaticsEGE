def f(n):
    s = ''
    while n > 0:
        s = str(n%7) + s
        n = n // 7

    return s

n = 6 * 343**5 + 5 * 49**7 - 50

s = f(n)
print(s.count('6'))
