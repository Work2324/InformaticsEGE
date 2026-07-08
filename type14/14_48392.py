for x in range(0, 9):
    for y in range(0, 9):
        if (int('2'+ str(y) + '66' + str(x), 9) + int(str(x) + '0' + str(y) + '1', 12)) % 170 == 0:
            print((int('2'+ str(y) + '66' + str(x), 9) + int(str(x) + '0' + str(y) + '1', 12)) / 170)
