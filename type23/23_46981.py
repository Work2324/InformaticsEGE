def f(n, k):
    if n > 11:
        return 0
    elif n == 11:
        return 1
    else:
        if k == 0:
            return f(n + 1, 0) + f(n + 2, 0) + f(n * 2, 1)
        else:
            return f(n + 1, 0) + f(n + 2, 0)

print(f(1, 0))
