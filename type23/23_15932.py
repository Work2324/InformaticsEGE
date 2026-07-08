def f(n, h):
    if n == h:
        return 1
    elif n > h or n == 29:
        return 0
    else:
        return f(n + 1, h) + f(n * 2, h) + f(n * 3, h)

print(f(2, 13) * f(13, 44))
