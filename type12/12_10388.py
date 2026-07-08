s = '5' * 54 + '7'

while s.count('722') > 0 or s.count('557') > 0:
    if s.count('722') > 0:
        s = s.replace('722', '57', 1)
    else:
        s = s.replace('557', '72', 1)

print(s)
