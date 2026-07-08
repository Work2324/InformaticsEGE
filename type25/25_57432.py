for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            s1 = '12' + str(x) + str(y) + '156'
            s2 = '12' + str(x) + str(y) + '1' + str(z) + '56'
            if int(s1) % 317 == 0:
                print(s1, int(s1) // 317)
            if int(s2) % 317 == 0:
                print(s2, int(s2) // 317)
