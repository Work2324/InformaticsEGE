for A in range(63, 0, -1):
    fl = True
    for x in range(0, 64):
        if ((x & 51 == 0) or ((x & 41 == 0 ) <= (x & A == 0))) == 0:
            fl = False
            break

    if fl:
        print(A)

#фуфло
