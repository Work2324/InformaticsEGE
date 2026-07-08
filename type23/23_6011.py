def f(n):
    if n == 22:
        return 1
    elif n > 22:
        return 0
    else:
        return f(n + 1) + f(n * 2)

print(f(2))
