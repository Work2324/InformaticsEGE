t = 0
for i in range(0, 10):
    if int('1' + str(i) + '49341') % 2023 == 0:
        t += 1
        print('1' + str(i) + '49341')

    for k in range(0, 1000):
        if int('1' + str(i) + '493' + str(k) + '41') % 2023 == 0:
            t += 1
            print('1' + str(i) + '493' + str(k) + '41')

    for k in range(0, 10):
        if int('1' + str(i) + '4930' + str(k) + '41') % 2023 == 0:
            t += 1
            print('1' + str(i) + '4930' + str(k) + '41')

    for k in range(0, 10):
        if int('1' + str(i) + '49300' + str(k) + '41') % 2023 == 0:
            t += 1
            print('1' + str(i) + '49300' + str(k) + '41')

print(t)
