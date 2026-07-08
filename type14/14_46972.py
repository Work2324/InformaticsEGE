def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n = n // 7

    return s

s = f(5 * 343**8 + 4 * 49**12 + 7**14 - 98)
mx = 0
ans = 0
for i in range(0, 7):
    temp = s.count(str(i))
    if temp > mx:
        mx = temp
        ans = i

print(ans)
